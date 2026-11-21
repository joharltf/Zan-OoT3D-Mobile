Second prerelease of **Zan — Ocarina of Time 3D — Mobile**.

This build adds the frame skip ON/OFF toggle that was verified on device. When
enabled, visual presentation is held on alternating frames while the guest
keeps running; Vulkan persistent scanout holds the last image instead of going
black. The change is staged until **RESTART GAME / RESTART SEKARANG** is pressed.

## Included

- Everything from v0.1.0-rc1.
- Frame skip toggle in the in-game Video tab, ZAN Tuner and F1 graphics panel.
- Clear letterbox bars in the NRI scanout path so scene/room fades no longer
  flicker a stale portrait image around the picture.
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
SHA-256: 5872c80c532dd7665e43ea545776a27450d1f28b4b6af7ce1131c9626f4d072b
```
