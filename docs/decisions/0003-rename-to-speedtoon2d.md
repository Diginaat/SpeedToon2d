# 0003 — Rename the application to SpeedToon2D

- **Status:** Accepted (step 1 of 3 done)
- **Date:** 2026-10-13

## Context

The owner asked for the software to be named **SpeedToon2D**. The name "Tahoma2D" was used in three ways:

1. As display text: window titles, dialogs, menus and messages.
2. As the **application identity**: `TVER::ToonzVersion::applicationName` in `toonz/sources/include/tversion.h`. This one string drives:
   - the window title,
   - the scene `generator` tag,
   - the Windows registry root,
   - the environment-variable names (`<NAME>ROOT`, `<NAME>PROFILES`, ...),
   - the Qt organisation and application names.
3. As build and packaging names: the `Tahoma2D` CMake target and `Tahoma2D.exe`, the `tahomastuff` folder, xdg/macOS bundle names and the splash and logo artwork.

## Decision

The rename happens in three steps.

**Step 1 (done).** Change the identity and the display text.

- `applicationName` and the organisation name become `SpeedToon2D`.
- The registry root becomes `SOFTWARE\SpeedToon2D\SpeedToon2D` (`toonz/sources/common/tapptools/tenv.cpp`).
- The environment variables become `SPEEDTOON2DROOT` and the `SPEEDTOON2D*` prefix, in `toonz/main.cpp`, `tcomposer`, `tcleanupper` and `tconverter`, so the app and its command-line render tools stay consistent.
- The default projects folder becomes `Documents\SpeedToon2D`.
- User-visible strings are updated: about, startup, tips, preferences, shortcuts, dialogs, splash messages and the file-type labels in the info viewer.

These are deliberately **not** changed in step 1:

- Upstream attribution: the "Tahoma2D License" link and the patron and sponsor text in `aboutpopup.cpp`.
- The "import settings from a Tahoma2D installation" preference text, which really does refer to Tahoma2D.
- The `Tahoma2D` shortcut preset name.
- The issue-tracker and update-checker texts and URLs (`crashhandler.cpp`, `mainwindow.cpp`, the update checker). They need fork URLs first.
- The `tahomastuff` folder name and the scene and file formats.

**Step 2 (todo).** Rename the build and packaging: the CMake target and exe `SpeedToon2D`, the xdg desktop and metainfo files, the macOS bundle, and `crashhandler.cpp:392`.

**Step 3 (todo).** Branding: new splash, startup and logo artwork, app icon (`toonz.rc`), `stuff/doc/*/tips.md`, issue and update URLs.

## Compatibility

- **Scenes:** fully compatible. The loader only checks the `generator` string for the substring `2.2` (`toonzscene.cpp`, around line 477). Warning: a future SpeedToon2D version string containing "2.2" would trigger that legacy path, so remove the check before using a 2.2 version number.
- **Portable mode** (`tahomastuff/` next to the exe) is unaffected.
- **Installed mode:** SpeedToon2D no longer reads Tahoma2D's registry or environment variables. It installs side by side with Tahoma2D. Settings can still be imported with the existing "import from another installation" feature in Preferences.
- **Translations:** the renamed `tr()` strings no longer match the `.ts` and `.qm` catalogues, so those strings show in English until the translations are regenerated.

## Risks

- Any external installer or script that sets `TAHOMA2DROOT` for a SpeedToon2D install must switch to `SPEEDTOON2DROOT`.
