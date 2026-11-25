#!/usr/bin/env python3
"""Build the GPL corresponding-source archive for a Zan binary release.

Usage:
    python3 scripts/package-source.py \
        --source-dir /path/to/Port-Native \
        --apk /path/to/Zan-OoT3D-Mobile-arm64.apk \
        --tag v0.1.0-rc3 \
        --out Zan-OoT3D-Mobile-v0.1.0-rc3-source.zip

The script refuses a dirty source tree and any path that looks like a ROM,
game dump, credential, signing key or prebuilt binary.
"""

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

REQUIRED_DOCS = (
    "LICENSE",
    "LICENSE_SCOPE.md",
    "THIRD_PARTY_NOTICES.md",
    "SOURCE_OFFER.md",
    "README.md",
    "ZELDAOOT3D_PATCH.md",
)

SENSITIVE = re.compile(
    r"(?:^|/)(?:\.git|build|release-desktop|out|dist)(?:/|$)",
    re.I,
)
SENSITIVE_NAME = re.compile(
    r"(?:^|/)(?:secrets?|credentials?|tokens?|keystores?|signing)(?:/|$)"
    r"|(?:^|[/_.-])(?:rom|roms|dump|dumped|decrypted|saves?)(?:[/_.-]|$)"
    r"|\.(?:jks|p12|pem|key|keystore)$",
    re.I,
)
BINARY_SUFFIX = {
    ".apk", ".so", ".a", ".o", ".dll", ".exe", ".dylib", ".appimage",
    ".zip", ".tar", ".gz", ".xz", ".7z", ".rar", ".jar", ".class",
    ".pyc", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".bin",
    ".dat", ".ctxb", ".zar", ".qbf", ".bps", ".ips",
}
MAX_BYTES = 5 * 1024 * 1024
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def git(source, *args):
    result = subprocess.run(
        ["git", "-C", str(source), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect(source):
    files = []
    rejected = []
    for raw in git(source, "ls-files", "-z").split("\0"):
        if not raw:
            continue
        relative = Path(raw)
        text = relative.as_posix()
        if SENSITIVE.search(text) or SENSITIVE_NAME.search(text):
            rejected.append((text, "sensitive-looking path"))
            continue
        if relative.suffix.lower() in BINARY_SUFFIX:
            rejected.append((text, "binary or game asset"))
            continue
        full = source / relative
        if not full.is_file():
            continue
        size = full.stat().st_size
        if size > MAX_BYTES:
            rejected.append((text, f"larger than {MAX_BYTES} bytes"))
            continue
        files.append((text, full))
    return files, rejected


def build_manifest(source, apk, tag, files, rejected, commit=None):
    patch = source / "ZELDAOOT3D_PATCH.md"
    upstream_commit = None
    if patch.is_file():
        match = re.search(r"upstream commit `([0-9a-f]{7,40})`", patch.read_text(encoding="utf-8"))
        if match:
            upstream_commit = match.group(1)

    return {
        "schema_version": 1,
        "tag": tag,
        "package": "org.zan.ocarinaoftime",
        "apk": {
            "filename": apk.name,
            "sha256": sha256(apk),
        },
        "source": {
            "repository": git(source, "remote", "get-url", "origin"),
            "branch": git(source, "rev-parse", "--abbrev-ref", "HEAD"),
            "commit": commit or git(source, "rev-parse", "HEAD"),
            "clean": not bool(git(source, "status", "--porcelain")),
        },
        "upstream": {
            "repository": "https://github.com/coccofresco/TriAevum",
            "commit": upstream_commit,
            "license": "GPL-3.0-or-later",
        },
        "included_file_count": len(files),
        "excluded": [
            "ROM images, decrypted game data, extracted game assets and save data",
            "signing keys, credentials and private tester data",
            "prebuilt binaries and build outputs",
            "iMMERSE / MXAO module (permission is exclusive to coccofresco/TriAevum)",
            "NVIDIA DLSS / NGX SDK binaries (separate license)",
        ],
        "rejected_paths": [{"path": p, "reason": r} for p, r in rejected],
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
    }


def write_zip(out, source, apk, tag, files, manifest):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, full in files:
            info = zipfile.ZipInfo(f"source/{name}", FIXED_TIME)
            info.external_attr = 0o644 << 16
            archive.writestr(info, full.read_bytes())

        for name in REQUIRED_DOCS:
            full = source / name
            if full.is_file():
                info = zipfile.ZipInfo(f"source/{name}", FIXED_TIME)
                info.external_attr = 0o644 << 16
                archive.writestr(info, full.read_bytes())

        info = zipfile.ZipInfo("release-manifest.json", FIXED_TIME)
        info.external_attr = 0o644 << 16
        archive.writestr(info, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

        info = zipfile.ZipInfo("BUILD.md", FIXED_TIME)
        info.external_attr = 0o644 << 16
        archive.writestr(info, BUILD.format(tag=tag, commit=manifest["source"]["commit"]))


BUILD = """# Building {tag}

This archive is the corresponding source for release `{tag}` (source commit
`{commit}`). It is buildable without a game dump; the game image is supplied by
the player at run time.

1. Use the Android instructions in `source/ZELDAOOT3D_PATCH.md` and
   `source/ports/android/INTRO.md`.
2. Keep the iMMERSE/MXAO module disabled. Its license permission was granted
   only to coccofresco/TriAevum and does not transfer to this fork.
3. Do not enable the NVIDIA DLSS/NGX module; its SDK has a separate license.
4. Do not bundle ROMs, extracted assets or optional GameBanana mods.

See `release-manifest.json` for the exact APK checksum and dependency
identities, and `source/LICENSE_SCOPE.md` for the license boundaries.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--apk", required=True, type=Path)
    parser.add_argument("--tag", required=True)
    parser.add_argument(
        "--commit",
        help="source commit actually used for the build (defaults to HEAD)",
    )
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    source = args.source_dir.resolve()
    apk = args.apk.resolve()
    out = args.out.resolve()

    if not (source / ".git").exists():
        print(f"not a git checkout: {source}", file=sys.stderr)
        return 1
    if not apk.is_file():
        print(f"APK not found: {apk}", file=sys.stderr)
        return 1

    missing = [name for name in REQUIRED_DOCS if not (source / name).is_file()]
    if missing:
        print(f"missing required documents: {', '.join(missing)}", file=sys.stderr)
        return 1

    if git(source, "status", "--porcelain"):
        print("source tree is dirty; commit or stash changes first", file=sys.stderr)
        return 1

    files, rejected = collect(source)
    if not files:
        print("no source files collected", file=sys.stderr)
        return 1

    manifest = build_manifest(source, apk, args.tag, files, rejected, args.commit)
    write_zip(out, source, apk, args.tag, files, manifest)
    print(
        f"wrote {out} — {len(files)} source files, "
        f"{len(rejected)} paths excluded, APK {manifest['apk']['sha256'][:12]}…"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
