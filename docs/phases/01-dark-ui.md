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
- [ ] 1.3 Icons. **Deferred by the owner on 2026-10-13.** The chosen source for later is Phosphor (MIT). The audit notes are below.
- [ ] 1.4 (in progress) Typography: check font sizes and clipping at 100%, 125%, 150% and 200% DPI.
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

### 1.3 Icon audit (deferred, findings only)
- **Two icon systems exist:**
  - *Theme widget icons*: 61 SVGs in `stuff/config/qss/Medium/imgs/{white,black}/`, referenced from QSS (checkboxes, sliders, combo arrows). They are per-theme.
  - *Application icons*: 588 SVGs in `toonz/sources/toonz/icons/dark/{actions,console,mimetypes,tools}/<size>/`, compiled in through `toonz.qrc`. They are **shared by all themes**.
- **Loading:** `main.cpp:271` calls `ThemeManager::buildIconPathsMap(":/icons")`, which maps file **basenames** to paths (the first entry wins, so names must be unique). `createQIcon(name)` in `toonzqt/gutil.cpp` loads `name`, `name_over` and `name_on`.
- **Colouring:** the icons are drawn in black. `ThemeManager::recolorBlackPixels` recolours every pure-black pixel to white or black according to the `iconTheme` preference. Imported icons must therefore use `#000` fills. Phosphor's `currentColor` must be replaced.
- **Implication for Phosphor:** replacing files in `icons/dark/` would change the icons of *every* theme. To keep the other themes unchanged, add an override icon directory that is scanned before `:/icons`, for example per theme or as an "icon set" preference. That needs a small C++ change in `main.cpp` and `ThemeManager`, plus an ADR.

### 1.4 DPI review (partial)
- **Method:** launch the Modern theme with `QT_SCALE_FACTOR` set to 1.25, 1.5 and 2, wait 25 s, then take a screenshot. The screen is 1920x1080. Modern overrides colours only, so the results apply to every theme.
- **Results:**
  - 1.25: text is readable. The fixed pixel geometry in `room1.ini` leaves the timeline too short, so layer rows are cut off ([img](img/01-dpi125.png)).
  - 1.5: one timeline row is visible. The startup dialog was not visible in the capture ([img](img/01-dpi150.png)).
  - 2.0: the viewer title text overlapped the title-bar buttons ([before](img/01-dpi200-before.png)), and the timeline collapsed.
- **Fixed:** `TPanelTitleBar::paintEvent` (`toonz/sources/toonz/pane.cpp`) now elides the title before the leftmost visible title-bar button. It used to elide at `width - 50`. At 2.0 the title now ends in "…" ([after](img/01-dpi200-after.png)). At 1.0 the full title is still shown.
- **Open:** room layouts collapse the timeline at 1.5 and above. That belongs to Phase 2 (workspace presets) or Phase 3 (minimum sizes). Also open: the startup dialog at 1.5 and above, and a menu, dialog and font-size pass.
