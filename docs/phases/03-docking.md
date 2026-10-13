# Phase 3 — Docking and panel management

- **Status:** not started. This phase needs owner approval before it begins.
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

_No entries yet._
