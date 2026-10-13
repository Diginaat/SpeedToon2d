# Handoff

_Rewrite this file at the end of every session._

## Session 2026-10-14 (9): Phase 4 simple-view paint optimisation

- Current dirty work in `toonz/sources/toonz/xshcellviewer.cpp`: `drawLevelCell` skips text-rectangle/font setup for zoomed-out simple-view marker cells.
- Build completed after stale `Tahoma2D.exe` processes blocked linking; renamed the locked old exe to `Tahoma2D.locktest.exe`, rebuilt, then removed the renamed file.
- Benchmark after change on `perf_timeline_50x300.tnz` with `-StepCount 120`: 100 full-area samples, mean 2.19 ms, median 2.12 ms, p95 2.71 ms, max 2.98 ms. Baseline was p95 3.04 ms.
- **Exact next action:** review diff, optionally run one visual smoke test in the timeline, then commit this as 4.5b.

## Session 2026-10-14 (8): Phase 4 paint baseline tooling

- Continued Phase 4 on `feature/04-timeline`.
- Current dirty work adds opt-in `SPEEDTOON2D_TIMELINE_PAINT_LOG` timing in `CellArea::paintEvent` and benchmark helpers in `test-scenes/tools/`.
- Build completed: `cmake --build toonz/build --config RelWithDebInfo --parallel` rebuilt `Tahoma2D.exe`.
- The first generated 50x2000 scene referenced missing `+drawings\perf.pli` files; the generator now writes real 1x1 raster frames and uses `perf_timeline_50x300.tnz`.
- Baseline benchmark on `toonz/build/RelWithDebInfo/tahomastuff/sandbox/scenes/perf_timeline_50x300.tnz`: 90 full-area samples, mean 2.41 ms, median 2.28 ms, p95 3.04 ms, max 3.62 ms. Numbers are in `docs/phases/04-timeline.md`.
- **Exact next action:** compare any timeline paint changes against this baseline, or commit the tooling first as 4.5a.

## Session 2026-10-14 (7): Phase 4 timeline start

- The owner said "go to phase 4". Phase 3 is paused and merged (`de1de51b6`). Branch: `feature/04-timeline`.
- 4.1 data-flow table and 4.2a themeable keyframe colours (`b7823b59c`). See `docs/phases/04-timeline.md`.
- **Test trick:** in the Modern Animation room at 1.0, click the viewer's diamond button at (347,728) to set a key on Col1 at frame 1. The key icon is then at (355,860) in the timeline.
- 4.3 audit: most keyframe interactions already exist (see the phase doc). 4.3a made the box-selection rectangle visible (`e78a5f2d4`).
- **Exact next action:** decide with the owner whether box selection should start from empty space in the key strip (design question). Otherwise do 4.4 playback or a 4.5 performance baseline.

## Session 2026-10-13 (6): Phase 3 docking start

- Merged Phase 2 into dev (`2f4946b0d`). Branch: `feature/03-docking`. `Default` stays the default room preset, because the owner has not decided.
- `DockWidget::fitToScreen()` keeps floating panels on screen (`828bc7a35`). `Esc` closes floating panels (`TPanel::keyPressEvent`). Both were tested at 1.0.
- **Exact next action:** 3.3 reset, save and restore workspace commands, or 3.2 header and minimum-size polish.

## Session 2026-10-13 (5): Phase 2 workspace

- The owner chose Phase 2. Phase 1 is paused and merged into `dev/ui-modernization` (`5ded1b9c1`). Branch: `feature/02-workspace`.
- Added the `Modern` room preset with an **Animation** room (`b0b810dcd`). It is data only, with no C++ change. The room format is documented in `docs/phases/02-workspace.md`.
- Tested at 1.0 only (the owner asked to skip scaling checks): load, quit, private copy saved, and relaunch restores the layout.
- Test profile: `CurrentRoomChoice=Modern`.
- **Exact next action:** ask the owner whether `Modern` should become the default preset, then merge `feature/02-workspace` into dev and propose Phase 3 (docking).

## Session 2026-10-13 (4): finish 1.4

- Scripted DPI tour. The capture uses PowerShell, `SendKeys` and `user32` mouse clicks. With `startupPopupEnabled=false` and `tipsPopupEnabled=false` in the test profile, the startup dialogs don't block the capture. **Do not send `Alt+F`**: it toggles viewer full screen.
- Fixes: menu shortcut gap (`2ae1a30d2`, `main.cpp`) and blue radio buttons in Modern (`5210bc18f`). Full findings are in `docs/phases/01-dark-ui.md` under 1.4.
- **Exact next action:** task 1.5, the visual review. Alternatively, rename step 2 (exe) if the owner prefers.

## Session 2026-10-13 (3): DPI fix and rename

- The owner deferred icons (1.3). The audit findings are in `docs/phases/01-dark-ui.md`.
- 1.4 DPI review using `QT_SCALE_FACTOR`. Fixed the title overlap (`5b991a955`, `toonz/sources/toonz/pane.cpp`).
- Renamed the app to **SpeedToon2D**, step 1 (`1017990f5`, [ADR 0003](../decisions/0003-rename-to-speedtoon2d.md)). Full build exit 0. Launch verified with the window title "SpeedToon2D 1.6.3".
- **Warning:** the exe is still `Tahoma2D.exe` (step 2), and the startup logo is still Tahoma artwork (step 3).
- **Exact next action:** rename step 2 (the CMake target and exe), or continue 1.4, whichever the owner prefers.

---


## Session 2026-10-13 (2): Phase 1 start

**Requested:** the owner approved Phase 1 ("go").

**Completed**

- Merged `feature/00-foundation` into `dev/ui-modernization` (`896d35abe`) and created `feature/01-dark-ui`.
- 1.1: design tokens in `docs/DESIGN-SYSTEM.md`, plus `docs/tools/contrast.py` (11 out of 11 WCAG checks pass) (`cda0142c2`).
- 1.2: new **Modern** theme, `stuff/config/qss/Medium/less/themes/Modern.less` compiled to `stuff/config/qss/Modern/Modern.qss` (`3a12df2e9`). It overrides variables only. No C++ changed and no other theme changed.

**Incomplete:** tasks 1.3 (icons), 1.4 (typography and DPI) and 1.5 (visual review).

**Files modified:** `docs/DESIGN-SYSTEM.md`, `docs/tools/contrast.py`, `docs/phases/{00-foundation,01-dark-ui}.md`, `docs/phases/img/01-modern-launch.png`, `docs/ROADMAP.md`, `MEMORY.md`, this file, `stuff/config/qss/Medium/less/themes/Modern.less`, `stuff/config/qss/Modern/Modern.qss`.

**Branch / commit:** `feature/01-dark-ui`. Nothing has been pushed.

**Commands**

```sh
# LESS compiler (local, not in the repo)
cd <scratch>/lessc && npm init -y && npm install less@4
cd stuff/config/qss/Medium/less && <scratch>/lessc/node_modules/.bin/lessc themes/Modern.less ../../Modern/Modern.qss
# Deploy the theme to the run folder and select it
cp -r stuff/config/qss/Modern toonz/build/RelWithDebInfo/tahomastuff/config/qss/
# then set CurrentStyleSheetName=Modern in tahomastuff/profiles/users/<user>/preferences.ini
```

**Build results:** no C++ changed, so no rebuild was needed. The lessc compile exits 0.

**Tests:** the app launches with Modern, and the main window renders and is readable (manual, screenshot). Not run: switching theme from the Preferences dialog, dialogs, DPI scaling.

**Warnings for the next agent**

- After editing `Medium.less` or `components/` or `layouts/`, recompile **all** six themes: Medium, Dark, Darker, Light, Neutral and Modern.
- The icon-theme heuristic in `PreferencesPopup::onStyleSheetTypeChanged` checks for the substring `imgs/black` in the QSS. Keep Modern on `imgs/white`.
- The test run folder's `preferences.ini` is set to Modern. Delete that line to go back to Dark.

**Exact next action:** get the owner's choice of icon approach for 1.3. Meanwhile, task 1.4 can start: launch with `QT_SCALE_FACTOR` set to 1.25, 1.5 and 2, take screenshots, and look for clipped text.
