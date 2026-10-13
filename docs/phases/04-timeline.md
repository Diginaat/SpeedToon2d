# Phase 4 — Horizontal timeline and keyframes

- **Status:** in progress (approved 2026-10-14). Phase 3 was paused to start it.
- **Branch:** `feature/04-timeline`

## Goal

Make the Timeline professional, with clearer keyframe editing. Keep exposure and keyframe semantics unchanged.

## Where to start (verified paths)

- `XsheetViewer` in `toonz/sources/toonz/xsheetviewer.{h,cpp}`. The Xsheet and the Timeline are **one widget** with two orientations.
- `toonz/sources/include/orientation.h` and `toonz/sources/toonzlib/orientation.cpp`.
- In `toonz/sources/toonz/`: `xshcellviewer`, `xshcolumnviewer`, `xshrowviewer`, `layerheaderpanel`, `frameheadgadget`, `keyframeselection` and `keyframemover`.
- Drawing exposures are `TXshCell`. Property keyframes are `TDoubleParam` on `TStageObject` channels.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [x] 4.1 Document the data flow: exposures compared with keyframes, selection, undo.
- [ ] 4.2 Appearance: ruler, keyframe glyphs, selection, row spacing, grid contrast, zoom and playhead.
- [ ] 4.3 (in progress) Keyframe interactions: multi-select, box select, move, copy and paste, keyboard navigation, context menus.
- [ ] 4.4 Playback: scrubbing, frame range display, onion-skin visibility.
- [ ] 4.5 Performance: measure painting on a large scene before and after.

## Acceptance criteria

- Existing scenes display correctly, and exposures stay exact.
- Keyframe edits are correct, and undo and redo work.
- The timeline stays responsive on large scenes. Performance is compared against a recorded baseline.

## Log

### 4.1 Data flow
There are two different kinds of timeline data. Never mix them up:

| Data | Model | Timeline UI | Copy, paste and undo |
|---|---|---|---|
| **Drawing exposures** (which drawing shows on which frame) | `TXshCell` in `TXshColumn` (`toonz/sources/toonzlib/txshcell.cpp`, `txsheet.cpp`) | `CellArea::drawLevelCell` and related (`toonz/sources/toonz/xshcellviewer.cpp`). Selection: `TCellSelection`. Dragging: `xshcellmover.cpp` and `xsheetdragtool.cpp` | `celldata.cpp`, `cellselectioncommand.cpp` |
| **Property keyframes** (position, rotation, scale and so on of a column or pegbar) | `TStageObject` channels, which are `TDoubleParam` keyframes (`toonz/sources/include/toonz/tstageobject.h`: `isKeyframe`, `getKeyframeRange`, `getKeyframeSpan`, `setKeyframeWithoutUndo`) | `CellArea::drawKeyframe` and `drawKeyframeLine` draw the diamonds, the interpolation lines, ease handles and the cycle toggle. Selection: `TKeyframeSelection` (`keyframeselection.cpp`). Dragging: `KeyframeMover` and `KeyframeMoverTool` (`keyframemover.cpp`) | `TKeyframeData` (MIME data). `PasteKeyframesUndo`, `DeleteKeyframesUndo` and `ShiftKeyframesUndo` are in `keyframeselection.cpp`; `UndoMoveKeyFrame` is in `keyframemover.cpp` |

- `TCellKeyframeSelection` combines both for mixed selections.
- The viewer's diamond button (`ViewerKeyframeNavigator`, `toonz/sources/include/toonzqt/keyframenavigator.h`) sets or removes a key on the current object at the current frame.
- The Xsheet and the Timeline are the same `XsheetViewer`. All geometry comes from `Orientation` (`toonz/sources/toonzlib/orientation.cpp`): `PredefinedRect::KEY_ICON`, `FRAME_MARKER_AREA` and so on. Horizontal-only tweaks are spread through the paint code as `!o->isVerticalTimeline()` adjustments, which also depend on the *Timeline layout* preference (`NoDragMinimum`, `Roomy`).
- Colours come from about 120 `XsheetViewer` Q_PROPERTYs set by QSS (`stuff/config/qss/Medium/less/layouts/xsheet.less`). Some colours were still hard-coded in C++. See 4.2a.

### 4.2a Themeable keyframe colours (`b7823b59c`)
- Keyframe diamonds and ease handles were hard-coded `Qt::white`, and selected keyframes were `QColor(85,157,255)`. Two new properties replace them: `XsheetViewer::KeyframeColor` and `SelectedKeyframeColor` (LESS `@xsheet-Keyframe-color` and `@xsheet-SelectedKeyframe-color`).
- The defaults equal the old values, so each existing theme's QSS gains only those two lines with identical colours. Modern uses `@modern-accent-line` for selected keyframes.
- **Test (1.0, Modern):** the viewer's diamond button set a key on Col1 at frame 1, which showed as a white diamond ([img](img/04-key-unselected.png)). Clicking it selected it, and it turned blue `#4a8fe7` ([img](img/04-key-selected.png)).
- **Not tested:** the ease handles. They need a two-key segment with easing.

### 4.3 Keyframe interactions: what already exists
- **Selection:** click selects a key. Ctrl+click toggles and Shift+click extends (`KeyframeMoverTool::onClick`, `keyframemover.cpp`).
- **Box selection:** press on an unselected key and drag (`rectSelect`). It only starts *on a key*; pressing on empty space selects cells instead.
- **Moving:** drag a selected key to move it. Ctrl copies, Shift inserts and Alt overwrites (`KeyframeMover` qualifiers). Undo is `UndoMoveKeyFrame`.
- **Ease handles:** drag the triangles (`makeKeyFrameHandleMoverTool`).
- **Combined cell and key selection:** Alt+drag on cells, or Ctrl+drag with drag bars enabled (`TCellKeyframeSelection`).
- **Navigation:** Next/Previous Key on Ctrl+. and Ctrl+, (`MI_NextKeyframe`, `MI_PrevKeyframe`). The context menu includes invert selection, among other options.

### 4.3a Visible box selection (`feat(timeline): make the keyframe box selection visible`)
- `KeyframeMoverTool::drawCellsArea` drew a black dashed rectangle, which was almost invisible on dark timelines. It now uses `SelectedKeyframeColor` with a 40/255 fill, and the rectangle is normalised.
- **Test (1.0, Modern):** set a key, press on it, then drag right across frames 1-5. A blue dashed box with a light fill is visible ([img](img/04-key-box-select.png)).
- **Possible follow-up:** start a box selection from empty space in the key strip, as in Harmony. This conflicts with cell selection in the same area, so it needs a design decision, for example a modifier key.

### Still hard-coded in `drawKeyframe` (candidates for later)
- The keyframe outline (`Qt::black`).
- The cycle-toggle button, drawn with white and black primitives.
- The sound and other column painters, not yet audited.
