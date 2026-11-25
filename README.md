# Zan — Ocarina of Time 3D — Mobile

![Zan — Ocarina of Time 3D — Mobile social preview](https://raw.githubusercontent.com/joharltf/Zan-Previews/main/oot3d-mobile/zan-mobile-social-preview.png)

This repo contains **only** release artifacts and documentation. It is not a source repo
and cannot be used to rebuild the APK.

See [LICENSE](LICENSE) before downloading. Redistribution, reverse engineering
and rebuilding are not permitted.

## Credits

This build is based on the recompilation engine and Forge runtime created by
[coccofresco](https://github.com/coccofresco). Credit and thanks go to him and
his contributors.

## Current prerelease

`v0.1.0-rc3` — see the [release](../../releases/tag/v0.1.0-rc3).

| Item | Value |
| --- | --- |
| Package | `org.zan.ocarinaoftime` |
| ABI | `arm64-v8a` |
| Minimum Android | 10 (API 29) |
| Renderer | Native Vulkan path with NRI where supported |
| Verified devices | Xiaomi `surya` and POCO X3 NFC (Snapdragon 732G / Adreno 618, Android 12, Vulkan 1.1); Redmi Note 9 (Helio G85 / Mali-G52); Nubia Neo 3 5G |
| Not yet device-verified | Other Helio G99 / Mali-G57 devices not individually tested |
| APK SHA-256 | `6951c0c8d244ca3221d2394663407d00139f4d12417af86d82cb88b8f02ef306` |

This is a **prerelease**. Stable `v0.1.0` will be published after qualification
on the remaining untested Mali devices.

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
