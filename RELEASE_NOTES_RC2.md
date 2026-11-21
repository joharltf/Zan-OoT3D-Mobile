Second prerelease of **Zan — Ocarina of Time 3D — Mobile**.

This build adds the frame skip ON/OFF toggle that was verified on device. When
enabled, visual presentation is held on alternating frames while the guest
keeps running; Vulkan persistent scanout holds the last image instead of going
black. The change is staged until **RESTART GAME / RESTART SEKARANG** is pressed.

## Included

- Everything from v0.1.0-rc1.
- Frame skip toggle in the in-game Video tab, ZAN Tuner and F1 graphics panel.
- Package/Docs internals use `org.zan.ocarinaoftime`.
- TriAevum engine and Forge runtime credit in README.

## Verified

- Frame skip row visible directly under Frame rate in Video.
- Toggle stages a graphics change and is applied after restart.
- Config persists `Graphics.FrameRate.Skip` in `zan.android.json`.
- Xiaomi `surya`, Snapdragon 732G / Adreno 618, Android 12, Vulkan 1.1.

## Integrity

```text
Zan-OoT3D-Mobile-arm64.apk
SHA-256: 732acc9b1d72a764f3386a7fb4001bef0b271bea27d2b512e78bb3327dbaf01d
```
