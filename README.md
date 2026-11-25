# Zan — Ocarina of Time 3D — Mobile

![Zan — Ocarina of Time 3D — Mobile social preview](https://raw.githubusercontent.com/joharltf/Zan-Previews/main/oot3d-mobile/zan-mobile-social-preview.png)

This repo contains **only** release artifacts and documentation. It is not a source repo
and cannot be used to rebuild the APK on its own; see [SOURCE_OFFER.md](SOURCE_OFFER.md)
for the corresponding source attached to each release.

See [LICENSE](LICENSE) before downloading. The third-party parts of the APK — including
the TriAevum engine — keep their own licenses, which are not restricted by this repo's
license.

## Credits

This build is derived from the recompilation engine, Forge runtime and Android work in
[coccofresco/TriAevum](https://github.com/coccofresco/TriAevum), licensed GPL-3.0-or-later.
Credit and thanks go to coccofresco and all contributors whose code and artwork are
listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and in the notices inside the APK.

The original games were created by Nintendo and Grezzo. No game data is bundled.

## Licensing and source

- [LICENSE](LICENSE) — terms for material authored by joharltf, with an explicit
  carve-out preserving GPL and other third-party rights.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — component licenses and boundaries.
  The full texts ship inside every APK under `assets/notices/`.
- [SOURCE_OFFER.md](SOURCE_OFFER.md) — how the GPL corresponding source for each
  release is published.

## Current prerelease

`v0.1.0-rc3` — see the [release](../../releases/tag/v0.1.0-rc3).

| Item | Value |
| --- | --- |
| Package | `org.zan.ocarinaoftime` |
| ABI | `arm64-v8a` |
| Minimum Android | 10 (API 29) |
| Renderer | Native Vulkan path with NRI where supported |
| Verified devices | POCO X3 NFC (Snapdragon 732G / Adreno 618, Android 12, Vulkan 1.1); Redmi Note 9 (Helio G85 / Mali-G52); Nubia Neo 3 5G (Unisoc T8300 / Mali-G57 MC2) |
| APK SHA-256 | `6951c0c8d244ca3221d2394663407d00139f4d12417af86d82cb88b8f02ef306` |

This build includes the `REPORT` tab with `/sdcard/OOTD/log.txt` and share
links, and the in-game `Resolution` row. The live performance overlay has been
removed so controller and touchscreen buttons are never captured. This is a
**prerelease**. Stable `v0.1.0` will be published after more device qualification.

## Install and test

1. Download `Zan-OoT3D-Mobile-arm64.apk` from Releases.
2. Allow installation from the file manager/browser on Android.
3. Install the APK. No ROM or game data is bundled.
4. Put the decrypt rom file in the internal storage "/OOT3D"
5. Play and wait for the build to run, and you can play it

## Bug reports

If a glitch or crash happens, attach this one automatically written file from
Discord; no menu action is needed:

```text
Android/data/org.zan.ocarinaoftime/files/data/logs/Zan-bug-report.txt
```

It is redacted: user paths, title folders and hashes are removed. Do not attach
your ROM or save files.
