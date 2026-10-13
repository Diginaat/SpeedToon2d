# Design system

These are the tokens for the **Modern** theme, a neutral graphite dark theme with a single blue accent, inspired by modern production tools.
Owner: Phase 1. The implementation is `stuff/config/qss/Medium/less/themes/Modern.less` (task 1.2).

## Principles

1. **Neutral surfaces, one accent.** Grey carries structure. Blue means "selected or focused". Every other colour carries a fixed meaning (status, keyframe, column type).
2. **Depth through lightness.** A darker surface sits further back: canvas < sunken < panel < raised < hover.
3. **Readable for long sessions.** Body text is never pure white on pure black. Small text meets WCAG AA (4.5:1).
4. **The theme does not override user preferences.** Font family and size come from *Preferences > Interface* (`interfaceFont`, `EnvSoftwareCurrentFontSize`, see `toonz/sources/toonz/main.cpp`), so the QSS sets no `font-family` or `font-size` for body text.

## How the theme pipeline works

- `Medium/less/Medium.less` defines about 300 variables with defaults. `main.less` pulls in the components and layouts that use them.
- A theme file in `Medium/less/themes/` imports `../Medium` and overrides variables. Its first line `// out: ../../../<Name>/<Name>.qss` names the output file.
- The app lists **every folder** in `<stuff>/config/qss/` as a theme (`Preferences` constructor, `toonz/sources/toonzlib/preferences.cpp`). Adding `qss/<Name>/<Name>.qss` therefore makes the theme selectable, with no C++ change needed.
- Compile with `lessc` (verified with less 4.9.1, which reproduces every committed `.qss` byte-for-byte apart from line endings):

  ```sh
  cd stuff/config/qss/Medium/less
  lessc themes/Modern.less ../../Modern/Modern.qss
  ```

## Colour tokens

Contrast is measured against **panel** (`#282a2e`) unless another surface is named. The script is `docs/tools/contrast.py`.

### Surfaces

| Token | Hex | Use | LESS variables |
|---|---|---|---|
| canvas | `#17181b` | gaps between docked panels, separators | `@dock-bg-color`, `@accent` (border colour, despite the name) |
| sunken | `#1f2124` | inputs, trees, tab bar, title bars | `@input-bg-color`, `@tree-bg-color`, `@tabbar-bg-color`, `@title-bg-color` |
| panel | `#282a2e` | default panel background | `@bg` |
| raised | `#383b40` | buttons | `@button-bg-color` |
| hover | `#43474d` | hovered buttons, scrollbar handles | `@button-bg-color-hover`, `@scrollbar-handle-bg-color-hover` |
| line | `#3a3d42` | input and menu borders | `@input-border-color`, `@menu-border-color` |

### Text

| Token | Hex | Contrast (panel / sunken) | Use |
|---|---|---|---|
| text | `#dfe1e5` | 11.0 / 12.3 | body text, values |
| text-secondary | `#a3a8b0` | 6.0 / 6.8 | tab labels, inactive titles, hints |
| text-disabled | `@text-color` faded to 40% | (exempt) | disabled controls |
| text-on-accent | `#ffffff` | 4.56 on `#3574d4` | selected items |

### Accent and states

| Token | Hex | Use |
|---|---|---|
| accent | `#3574d4` | selection fills, checked tools, the active room tab, checked checkboxes |
| accent-line | `#4a8fe7` (4.36:1) | focus rings, dock drop targets, selected schematic links |
| accent-secondary | `rgba(255,255,255,0.08)` | secondary or hover highlight in lists |
| warning | `#e3a33b` (6.6:1) | warnings, status highlight |
| error | `#ef6b63` (4.8:1) | error labels and text |
| success | `#3fb950` (5.7:1) | progress bars, the "render done" state |
| lock | `#c34040` | lock toggles. It is used as a fill behind a white icon, never as text. |

### Animation semantics (kept from upstream)

These colours carry meaning that users already know, so the Modern theme does **not** change them:

- Keyframes: `@keyframe-total-color: #be7323` (orange) and the in-between colour.
- Xsheet column types: `@xsheet-LevelColumn-color`, `@xsheet-VectorColumn-color` and the rest.
- Schematic node types: `@schematic-*Color`.

Changing them is a Phase 4 or Phase 6 decision.

## Shape and spacing

| Token | Value | Variables |
|---|---|---|
| radius-small | 2 px | `@input-border-radius`, `@checkbox-border-radius` |
| radius-scroll | 4 px | `@scrollbar-handle-radius` |
| scrollbar margin | 3 px | `@scrollbar-handle-margin` |
| spacing | unchanged from upstream in 1.2 | revisit in task 1.4 after the DPI review |

## Icons (task 1.3)

The existing icons are SVGs in `stuff/config/qss/Medium/imgs/{white,black}/`. Modern uses the `white` set, as Dark does. The audit and redraw are task 1.3.

## Tooltips and scrollbars

- Tooltip: background `#111214`, border `#3d4046`, text `#dfe1e5` (14.3:1).
- Scrollbar: track `#1f2124`, handle `#3d4046`, hover `#4b4f56`, pressed `#5a5f67`, radius 4, no border.
