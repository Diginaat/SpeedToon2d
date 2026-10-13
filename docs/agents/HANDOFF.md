# Handoff

_Rewrite this file at the end of every session._

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
