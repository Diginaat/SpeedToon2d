# Phase 3 — Docking and panel management

- **Status:** in progress (approved 2026-10-13).
- **Branch:** `feature/03-docking`

## Goal

Make docking, floating panels and layout management clearer and more robust.

## Where to start (verified paths)

- `toonz/sources/toonzqt/docklayout.{h,cpp}`: a custom framework, **not** `QDockWidget`.
- `toonz/sources/toonzqt/tdockwindows.{h,cpp}` (`TMainWindow`, `TDockWidget`).
- `toonz/sources/toonz/pane.{h,cpp}` (`TPanel`, `TPanelTitleBar`) and `toonz/sources/toonz/floatingpanelcommand.cpp`.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 3.1 Audit the docking architecture and record the findings here.
- [ ] 3.2 Improve visual drop targets, dock and undock feedback, headers, resizing and minimum sizes. Make one change at a time.
- [ ] 3.3 Add reset, save and restore workspace, multi-monitor support, and recovery after a monitor disconnect.
- [ ] 3.4 Stress-test repeated dock and undock. Check object lifetimes and ownership of floating windows.

## Acceptance criteria

- Docking and floating work. The layout restores reliably.
- Repeated docking and undocking does not crash.
- Panels never stay off-screen after a monitor is removed.

## Log

### 3.1 Audit (floating panels)
- Floating panels are `TPanel`s (derived from `TDockWidget`, then `DockWidget`) that have been undocked from the room's `DockLayout`.
- They are opened by `OpenFloatingPanel::getOrOpenFloatingPanel` (`toonz/sources/toonz/floatingpanelcommand.cpp`).
- Their geometry is saved in `profiles/users/<user>/popups.ini` under `[Panels]/<type>/geometry` and restored by `TPanel::restoreFloatingPanelState`.
- Floating panels that belong to a room are restored by `DockLayout::restoreState`.
- **Problems found:**
  - A saved geometry was accepted if it touched the screen at all, so panels could open mostly off-screen.
  - Only *fully* off-screen panels were recovered, and they went to absolute `(50,50)`.
  - A new instance was offset +30 px without a bounds check.
  - `activateWidget` centred panels using primary-screen coordinates, which is wrong on a second monitor.
  - `restoreState` tested `m_saveIndex > 0`, so a floating panel stored at index 0 was never restored as floating.
  - `Esc` did nothing in floating panels.

### 3.3 Monitor and off-screen recovery (`828bc7a35`)
- New `DockWidget::fitToScreen()` (`toonz/sources/toonzqt/dockwidget.cpp`) picks the screen that shows most of the panel. If none does, it uses the panel's current screen. It then shrinks the panel to that screen's available area if needed and moves it fully inside.
- It is called on open, reuse, activate and room restore. The two bugs above (index 0, secondary-monitor centring) are fixed on the same paths.
- **Test (1.0):** `popups.ini` was seeded with `OutputSettingsPanel\geometry=@Rect(1600 800 700 600)`, which hangs off the bottom-right. Ctrl+O then opened Render Settings at full size, fully on screen and above the taskbar ([img](img/03-floating-fit.png)).
- **Not tested:** real multi-monitor setups and monitor disconnects. Only one monitor was available. The logic handles them, but they have not been verified.

### Escape closes floating panels (`TPanel::keyPressEvent`)
- `Esc` with no modifiers hides a floating panel through the same path as the close button. Children that use `Esc` get it first.
- **Test (1.0):** Ctrl+O opened Render Settings, `Esc` closed it, and Ctrl+O opened it again.

### Remaining
- 3.2: visual docking feedback. The Modern theme already shows blue drop targets (`@dock-placeholder-color`). Header consistency and minimum sizes are still to do.
- 3.3: reset, save and restore workspace commands.
- 3.4: dock and undock stress test.
- Not docking work, but logged: `Alt+F` (viewer full screen) blocks the File menu key.
