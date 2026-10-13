# Phase 1 — Modern dark UI, icons, typography

- **Status:** in progress (approved 2026-10-13).
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

- [x] 1.1 Define tokens in [DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md).
- [x] 1.2 Add `themes/<NewName>.less`, generate its QSS and make it selectable in Preferences.
- [ ] 1.3 Audit icons, then redraw them consistently using redistributable licences only.
- [ ] 1.4 Typography: check font sizes and clipping at 100%, 125%, 150% and 200% DPI.
- [ ] 1.5 Visual review of every main panel. Save before and after screenshots in `docs/phases/img/`.

## Acceptance criteria

- The new theme is selectable, and every existing theme still works.
- No unreadable text or invisible icons. No broken layouts at the tested DPIs.
- A before and after comparison is documented.

## Log

### 1.1 Design tokens (`cda0142c2`)
The tokens are in [DESIGN-SYSTEM.md](../DESIGN-SYSTEM.md). `python docs/tools/contrast.py` passes 11 out of 11 checks.

### 1.2 Modern theme
- **What:** a new theme `Modern`. The source is `stuff/config/qss/Medium/less/themes/Modern.less` and the output is `stuff/config/qss/Modern/Modern.qss`. Only variables are overridden, so no layout or component LESS changed and no C++ changed.
- **Why:** to give a neutral graphite UI with a single blue selection accent instead of the Tahoma magenta.
- **How it becomes selectable:** `Preferences` lists every folder in `qss/` (`toonz/sources/toonzlib/preferences.cpp`, around line 345).
- **Build:** `lessc themes/Modern.less ../../Modern/Modern.qss` with less 4.9.1 gives exit 0. The only warning, `extend ' .QPushButton' has no matches`, also appears for every existing theme.
- **Icon theme:** the `PreferencesPopup::onStyleSheetTypeChanged` heuristic picks white icons for Modern, the same as for Dark: no `imgs/black` in the QSS.
- **Existing themes:** their LESS and QSS files are unchanged. lessc reproduces all five byte-for-byte, apart from CRLF.
- **Tested (manual):** with `CurrentStyleSheetName=Modern` set in the portable `preferences.ini`, the app launched with the theme applied. The main window, menus, room tabs, toolbar, viewer, timeline, style editor and startup dialog are readable, and no icons are invisible. Screenshot: [img/01-modern-launch.png](img/01-modern-launch.png). The Dark baseline is [img/00-baseline-launch.png](img/00-baseline-launch.png).
- **Not run:** switching theme from the *Preferences* dialog at runtime; the remaining dialogs, Preferences, the schematic and the function editor; DPI scaling. These belong to task 1.5 and task 1.4.
