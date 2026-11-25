# Third-party notices

The prebuilt APK contains components developed by other people. They remain
under their own licenses; this repository does not relicense them.

**Authoritative texts:** every release APK carries the complete notices at
`assets/notices/` — including `LICENSE` (GPL-3.0), `docs/LICENSE_SCOPE.md`,
`docs/THIRD_PARTY_NOTICES.md`, `docs/SOURCE_OFFER.md` and the individual texts
under `LICENSES/`. The summary below is for readers of the web page.

| Component | License | Text in the APK |
| :--- | :--- | :--- |
| TriAevum engine, Forge runtime and the Android portability changes | GPL-3.0-or-later | `assets/notices/LICENSE` |
| Azahar / Citra-derived code, PICA decompiler, touch overlay | GPL-2.0-or-later | `assets/notices/LICENSES/GPL-2.0-or-later.txt` |
| libultraship (`three_ds_recomp_runtime` submodule) | MIT | `assets/notices/LICENSES/libultraship-MIT.txt` |
| SDL2, SDL_GameControllerDB | zlib | `assets/notices/LICENSES/SDL2-zlib.txt`, `SDL-GameControllerDB-zlib.txt` |
| NVIDIA NRI, FidelityFX SDK, Godot-derived shader, Aurora, nlohmann/json | MIT / CC0 | `assets/notices/LICENSES/` |
| zstd, nihstro, Vulkan loader components | BSD | `assets/notices/LICENSES/zstd-BSD-3-Clause.txt`, `nihstro-BSD-3-Clause.txt` |
| Fira Sans Condensed font atlas | SIL OFL 1.1 | `assets/notices/LICENSES/FiraSans-OFL.txt` |
| Rust Forge crates | various (MIT / Apache-2.0 / others) | `assets/notices/LICENSES/Rust-Forge-crates.md` |
| SingleScreen 3.0 UI files | author's terms, permission recorded upstream | `assets/notices/LICENSES/SingleScreen-3.0.md` |
| iMMERSE / MXAO (Pascal Gilcher) | "all rights reserved", permission granted only to the TriAevum project | `assets/notices/LICENSES/iMMERSE-LICENSE.txt`, `iMMERSE-MXAO.md` |

Two important boundaries:

- **iMMERSE / MXAO is not used in the Android build.** Its permission was
  granted exclusively to coccofresco/TriAevum and does not transfer to forks.
  The text is shipped only for transparency; the module is disabled.
- **NVIDIA DLSS / NGX is not used in the Android build.** Its notice is
  shipped for transparency; the SDK binaries are not part of the APK.

Optional mods from GameBanana — **OoT3D Vanilla UI/HUD** and **Vanilla+ — Link
Remodel And HD Item Models** by their respective authors — are CC BY-NC-ND 4.0
and are **not bundled**. They are downloaded by the user, from the author's
original archive, only if the user enables them.

No permission is granted here for Nintendo or Grezzo ROMs, executable code,
assets, firmware, keys or trademarks. The original games were created by
Nintendo and Grezzo; users supply their own legally obtained game dump.

Full upstream provenance, including Shipwright, Azahar, libultraship, SDL,
NRI, FidelityFX, the TopScreen/SingleScreen credits and all component authors,
is in the upstream project: https://github.com/coccofresco/TriAevum and in the
`assets/notices/docs/THIRD_PARTY_NOTICES.md` file inside the APK.

Special thanks to [coccofresco](https://github.com/coccofresco) and every
contributor whose work this build derives from.
