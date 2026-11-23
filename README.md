# Zan — Ocarina of Time 3D — Mobile

![Zan — Ocarina of Time 3D — Mobile social preview](https://raw.githubusercontent.com/joharltf/Zan-Previews/main/oot3d-mobile/zan-mobile-social-preview.png)

This repo contains **only** release artifacts and documentation. It is not a source repo
and cannot be used to rebuild the APK.

See [LICENSE](LICENSE) before downloading. Redistribution, reverse engineering
and rebuilding are not permitted.

## Credits

This build is based on the **TriAevum** engine and Forge runtime. Credit and
thanks go to the TriAevum project and its contributors.

## Current prerelease

`v0.1.0-rc2` — see the [release](../../releases/tag/v0.1.0-rc2) or [release notes](RELEASE_NOTES_RC2.md).

| Item | Value |
| --- | --- |
| Package | `org.zan.ocarinaoftime` |
| ABI | `arm64-v8a` |
| Minimum Android | 10 (API 29) |
| Renderer | Native Vulkan path with NRI where supported |
| Verified device | Xiaomi `surya`, Snapdragon 732G / Adreno 618, Android 12, Vulkan 1.1 |
| Not yet device-verified | Helio G85/G99, Mali-G52/G57 class |
| APK SHA-256 | `5872c80c532dd7665e43ea545776a27450d1f28b4b6af7ce1131c9626f4d072b` |

This is a **prerelease**. Stable `v0.1.0` will be published after more device
qualification, especially on Mali.

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
