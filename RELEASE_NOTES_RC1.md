First public prerelease of **Zan — Ocarina of Time 3D — Mobile**.

## What is included

- Native Vulkan renderer for Android 10+ `arm64-v8a`.
- Game-styled ImGui Performance/Graphics panel, F1 swipe scrolling and grip move.
- FPS/CPU/GPU HUD; GPU uses a two-query whole-frame Vulkan timestamp.
- Frame skip ON/OFF toggle in the Video, ZAN Tuner and F1 graphics panels.
- `Pilih backend renderer` preference (backend for next launch; no `.so`/ICD import).
- Automatic single-file redacted bug log: `Zan-bug-report.txt`.
- Vendor/driver detection for ARM Mali and Qualcomm Adreno in diagnostics.

## Verified

- Xiaomi `surya`, Snapdragon 732G / Adreno 618, Android 12, Vulkan 1.1.128.
- GPU timing and automatic bug report verified on device.
- No ROM, decrypted game data, extracted assets or saves bundled.

## Not yet verified

- Helio G85/G99 with Mali-G52/G57 class GPUs. Vendor detection and safe logging
  are present, but real device numbers are still needed.
- This is why this is `v0.1.0-rc1`, not stable `v0.1.0`.

## Install

Download the APK from this prerelease. Supply your own legally obtained
decrypted game image locally through the in-app Forge. See the repository
`LICENSE` before use; rebuilding and redistribution are not permitted.

## Integrity

```text
Zan-OoT3D-Mobile-arm64.apk
SHA-256: 732acc9b1d72a764f3386a7fb4001bef0b271bea27d2b512e78bb3327dbaf01d
```
