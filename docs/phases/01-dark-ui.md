# Phase 1 — Modern dark UI, icons, typography

- **Status:** not started. This phase needs owner approval before it begins.
- **Branch:** `feature/01-dark-ui`

## Goal

Add a new, selectable dark theme with consistent icons and typography. Do not touch the animation engine.

## Where to start (verified paths)

- LESS source: `stuff/config/qss/Medium/less/` (variant themes in `themes/`).
- QSS loader: `Preferences::getCurrentStyleSheet()` in `toonz/sources/toonzlib/preferences.cpp`.
- Icons: `stuff/config/qss/Medium/imgs/`.
- Colours set through Q_PROPERTY: `toonz/sources/toonz/xsheetviewer.h` (121 Q_PROPERTY lines).

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 1.1 Define tokens in [DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md).
- [ ] 1.2 Add `themes/<NewName>.less`, generate its QSS and make it selectable in Preferences.
- [ ] 1.3 Audit icons, then redraw them consistently using redistributable licences only.
- [ ] 1.4 Typography: check font sizes and clipping at 100%, 125%, 150% and 200% DPI.
- [ ] 1.5 Visual review of every main panel. Save before and after screenshots in `docs/phases/img/`.

## Acceptance criteria

- The new theme is selectable, and every existing theme still works.
- No unreadable text or invisible icons. No broken layouts at the tested DPIs.
- A before and after comparison is documented.

## Log

_No entries yet._
