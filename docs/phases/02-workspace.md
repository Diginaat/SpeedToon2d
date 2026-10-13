# Phase 2 — Harmony-inspired workspace preset

- **Status:** not started. This phase needs owner approval before it begins.
- **Branch:** `feature/02-workspace`

## Goal

Add an opt-in animation room preset: viewer in the centre, tools on the left, timeline and layers at the bottom, properties on the right, and the node editor one click away.

## Where to start (verified paths)

- Room presets: `stuff/profiles/layouts/rooms/{Default,OpenToonz,StudioGhibli}/` (`layouts.txt` plus `roomN.ini`).
- `Room` and `MainWindow::readSettings`/`writeSettings`: `toonz/sources/toonz/mainwindow.{h,cpp}`.
- Panel ids: `TPanelFactory("...")` in `toonz/sources/toonz/tpanels.cpp`.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 2.1 Document how rooms, `layouts.txt` and the `hierarchy=` dock-tree encoding work.
- [ ] 2.2 Add a new preset folder with the modern layout.
- [ ] 2.3 Let users switch between the original and modern layouts.
- [ ] 2.4 Verify that the layout persists across restarts using the existing settings.

## Acceptance criteria

- The workspace opens correctly and is restored after a restart.
- Existing presets still work. Scene data does not change.

## Log

_No entries yet._
