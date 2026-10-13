# MEMORY.md — project working memory

Keep this file short and factual. Put detail in `docs/`. Update it whenever the state changes.

## Project identity

SpeedToon2D is a fork of Tahoma2D 1.6.3, which is itself based on OpenToonz. It is being modernised into a Harmony-inspired 2D animation tool, one verified phase at a time.
Licence: BSD-3 ([LICENSE.txt](LICENSE.txt)). Mission and rules: [AGENTS.md](AGENTS.md).

## Current status

- **Phase:** 4, Timeline ([docs/phases/04-timeline.md](docs/phases/04-timeline.md)), on branch `feature/04-timeline`. 4.1 (data flow) is done, and 4.2a (themeable keyframe colours, `b7823b59c`) is done.
- Phases 1 and 3 are paused but merged into dev (`de1de51b6`). Phase 2 is done.
- The owner asked to skip DPI and scaling checks from now on: test at 1.0 only.
- **State:** 1.1 and 1.2 are done. 1.3 (icons) was deferred by the owner; Phosphor is chosen for later. 1.4 is done. The step 1 rename to SpeedToon2D is done (`1017990f5`).
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
- 1.4: panel titles are elided before the title-bar buttons (`5b991a955`), menu labels no longer touch their shortcuts (`2ae1a30d2`), and Modern radio buttons are blue (`5210bc18f`).
- Rename to SpeedToon2D, step 1 (`1017990f5`). Full build passes, and the window title is "SpeedToon2D 1.6.3".

## Active problems

- The baseline test scene has not been created yet. It needs the GUI ([docs/TESTING.md](docs/TESTING.md#baseline-test-scene)).
- There are no automated tests, and the manual checklist has not been run yet.
- `ffmpeg` and `rhubarb` are not deployed in the local run folder.

## Important decisions

- [ADR 0001](docs/decisions/0001-ui-architecture.md): extend the existing Qt 5 widgets, LESS themes and docking. No framework swap.
- [ADR 0003](docs/decisions/0003-rename-to-speedtoon2d.md): the app identity is now `SpeedToon2D` (registry, env vars `SPEEDTOON2D*`, titles). The exe and branding renames are still to do.
- [ADR 0002](docs/decisions/0002-branch-and-upstream-strategy.md): `upstream` = tahoma2d, `opentoonz` = reference remote. Never commit to `master`.
- The owner removed Tahoma2D's `AI_POLICY.md`, `CHANGELOG.md` and `.vscode/settings.json` from the fork, along with the restrictive `AGENTS.md` and `CLAUDE.md`, which were replaced.

## Next actions

1. Rename step 2: CMake target and exe `SpeedToon2D.exe`, xdg and macOS packaging (ADR 0003).
2. Task 1.5: visual review of the dialogs, schematic and function editor. The scripted capture approach is described in the 1.4 log.
3. Task 1.5: visual review of the dialogs, Preferences, schematic and function editor. This needs GUI interaction.
4. Owner: create the baseline test scene (TESTING.md).

## Last verified state

- Code baseline `3f2dde0af` (upstream, unmodified source): RelWithDebInfo build exit 0 (0 errors and 1729 warnings). The app launches.
- `3a12df2e9` (feature/01-dark-ui): only LESS and QSS changed, so no rebuild was needed. With the Modern theme the app launches and the main window renders (**pass**). Theme switching in the Preferences dialog: **not run**.
- Tests: automated **none exist**. Other manual checks: **not run**.
