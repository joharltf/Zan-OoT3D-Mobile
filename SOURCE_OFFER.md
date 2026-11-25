# Corresponding source offer

The Android build in this repository's releases is a derivative of
[coccofresco/TriAevum](https://github.com/coccofresco/TriAevum), whose code is
GPL-3.0-or-later. In accordance with that license, every binary release is
accompanied by the corresponding source.

## What is published

Each release on the [releases page](../../releases) has, alongside the APK:

- `Zan-OoT3D-Mobile-<tag>-source.zip` — the exact source tree used to build
  that release, plus its license texts and notices;
- `release-manifest.json` (inside the archive) — the release tag, APK SHA-256,
  source repository, branch and commit, the upstream commit this fork is based
  on, and the list of excluded material.

The archive is buildable without a game dump. It follows the upstream
precompiled-release model: generic runtime source and the generated title
source used for the shipped package are kept separate, and no ROM input or
extracted game asset is included.

## What is excluded, and why

The archive intentionally excludes ROMs, decrypted game data, extracted game
assets, save data, signing keys, credentials and private tester data. These
are either user-supplied locally or belong to Nintendo/Grezzo and are not
licensed for redistribution.

The iMMERSE/MXAO module and NVIDIA DLSS/NGX binaries are excluded: their
licenses do not permit redistribution by this fork. Their notice texts are
included for transparency.

## Regenerating an archive

The script `scripts/package-source.py` in this repository builds the archive
from a checkout of the `zeldaoot3d` source branch and the matching APK:

```sh
python3 scripts/package-source.py \
  --source-dir /path/to/Port-Native \
  --apk /path/to/Zan-OoT3D-Mobile-arm64.apk \
  --tag v0.1.0-rc3 \
  --out Zan-OoT3D-Mobile-v0.1.0-rc3-source.zip
```

Then attach the resulting zip to the matching release. The script refuses to
run if the source tree is missing its license/scope documents or if a
sensitive-looking path is present.

## Upstream source

The base project source, its own source offers and its release manifests are
at https://github.com/coccofresco/TriAevum.
