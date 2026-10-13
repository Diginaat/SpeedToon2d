# MEMORY.md — project working memory

Keep this file short and factual. Put detail in `docs/`. Update it whenever the state changes.

## Project identity

SpeedToon2d is a fork of Tahoma2D 1.6.3, which is itself based on OpenToonz. It is being modernised into a Harmony-inspired 2D animation tool, one verified phase at a time.
Licence: BSD-3 ([LICENSE.txt](LICENSE.txt)). Mission and rules: [AGENTS.md](AGENTS.md).

## Current status

- **Phase:** 0, Foundation ([docs/phases/00-foundation.md](docs/phases/00-foundation.md)).
- **State:** the build and launch are verified, and the docs are in place. The baseline test scene is missing.
- **Next phase (1, dark UI):** waiting for owner approval.

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

- Phase 0 docs, remotes and branches. Commits are on `feature/00-foundation`; see `git log dev/ui-modernization..feature/00-foundation`.

## Active problems

- The baseline test scene has not been created yet. It needs the GUI ([docs/TESTING.md](docs/TESTING.md#baseline-test-scene)).
- There are no automated tests, and the manual checklist has not been run yet.
- `ffmpeg` and `rhubarb` are not deployed in the local run folder.

## Important decisions

- [ADR 0001](docs/decisions/0001-ui-architecture.md): extend the existing Qt 5 widgets, LESS themes and docking. No framework swap.
- [ADR 0002](docs/decisions/0002-branch-and-upstream-strategy.md): `upstream` = tahoma2d, `opentoonz` = reference remote. Never commit to `master`.
- The owner removed Tahoma2D's `AI_POLICY.md`, `CHANGELOG.md` and `.vscode/settings.json` from the fork, along with the restrictive `AGENTS.md` and `CLAUDE.md`, which were replaced.

## Next actions

1. Owner: create the baseline test scene in the GUI, following the TESTING.md spec, and run the manual checklist once.
2. Owner: approve Phase 1. Then merge `feature/00-foundation` into `dev/ui-modernization`.
3. Phase 1, task 1.1: define design tokens in `docs/DESIGN-SYSTEM.md`.

## Last verified state

- Code baseline `3f2dde0af` (upstream, unmodified source): RelWithDebInfo build exit 0 (0 errors and 1729 warnings). The app launches.
- Tests: automated **none exist**. Manual: launch **pass**. All other checks are **not run**.
