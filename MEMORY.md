# MEMORY.md — project working memory

Keep this file short and factual. Put detail in `docs/`. Update it whenever the state changes.

## Project identity

SpeedToon2d is a fork of Tahoma2D 1.6.3, which is itself based on OpenToonz. It is being modernised into a Harmony-inspired 2D animation tool, one verified phase at a time.
Licence: BSD-3 ([LICENSE.txt](LICENSE.txt)). Mission and rules: [AGENTS.md](AGENTS.md).

## Current status

- **Phase:** 1, Dark UI ([docs/phases/01-dark-ui.md](docs/phases/01-dark-ui.md)), on branch `feature/01-dark-ui`.
- **State:** 1.1 (tokens) and 1.2 (Modern theme) are done. 1.3 (icons) waits on an owner decision about the icon source and licence.
- Phase 0 is merged into `dev/ui-modernization` (`896d35abe`). The test scene is deferred.

## Environment (verified 2026-10-13)

- Windows 11 IoT Enterprise LTSC 2024 (10.0.26100), x64.
- Visual Studio 18 (2026) Community, built with toolset **v143** (MSVC 14.44). CMake 4.4.4. Git 2.55. Git LFS 3.7.1 (unused).
- Qt 5.15.2 WinTab build (`thirdparty/qt/5.15.2_wintab/msvc2019_64`), Boost 1.87.0 headers, OpenCV 4.11.0 (`vc16`). All are git-ignored.
- Configure, build and run commands: [docs/BUILD-WINDOWS.md](docs/BUILD-WINDOWS.md).

## Architecture summary

- Libraries, from bottom to top: `tnzcore` → `tnzbase` → `tnzext` → `toonzlib` (scene model) → `toonzqt` (widgets) → `tnztools` → `toonz` (app).
- Themes: LESS in `stuff/config/qss/Medium/less/`. Rooms: `stuff/profiles/layouts/rooms/`. Docking: `toonzqt/docklayout.cpp`. Timeline: `toonz/xsheetviewer.cpp` (the same widget as the Xsheet). Schematic: `toonzqt/*schematic*`. Rigging: `tnztools/skeletontool`, `plastictool`, `toonzlib/ik*`.
- Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Completed work

- Phase 0: docs, remotes, branches and a verified build (merge `896d35abe`).
- 1.1 design tokens and contrast checker (`cda0142c2`).
- 1.2 Modern theme: `themes/Modern.less` and `qss/Modern/Modern.qss` (`3a12df2e9`).

## Active problems

- The baseline test scene has not been created yet. It needs the GUI ([docs/TESTING.md](docs/TESTING.md#baseline-test-scene)).
- There are no automated tests, and the manual checklist has not been run yet.
- `ffmpeg` and `rhubarb` are not deployed in the local run folder.

## Important decisions

- [ADR 0001](docs/decisions/0001-ui-architecture.md): extend the existing Qt 5 widgets, LESS themes and docking. No framework swap.
- [ADR 0002](docs/decisions/0002-branch-and-upstream-strategy.md): `upstream` = tahoma2d, `opentoonz` = reference remote. Never commit to `master`.
- The owner removed Tahoma2D's `AI_POLICY.md`, `CHANGELOG.md` and `.vscode/settings.json` from the fork, along with the restrictive `AGENTS.md` and `CLAUDE.md`, which were replaced.

## Next actions

1. Owner: choose the icon approach for task 1.3 (custom redraw, or an open icon set and its licence).
2. Task 1.4: DPI review. Launch with `QT_SCALE_FACTOR=1.25/1.5/2` and take screenshots.
3. Task 1.5: visual review of the dialogs, Preferences, schematic and function editor. This needs GUI interaction.
4. Owner: create the baseline test scene (TESTING.md).

## Last verified state

- Code baseline `3f2dde0af` (upstream, unmodified source): RelWithDebInfo build exit 0 (0 errors and 1729 warnings). The app launches.
- `3a12df2e9` (feature/01-dark-ui): only LESS and QSS changed, so no rebuild was needed. With the Modern theme the app launches and the main window renders (**pass**). Theme switching in the Preferences dialog: **not run**.
- Tests: automated **none exist**. Other manual checks: **not run**.
