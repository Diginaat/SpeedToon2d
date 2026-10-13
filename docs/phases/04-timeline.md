# Phase 4 — Horizontal timeline and keyframes

- **Status:** not started. This phase needs owner approval before it begins.
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

- [ ] 4.1 Document the data flow: exposures compared with keyframes, selection, undo.
- [ ] 4.2 Appearance: ruler, keyframe glyphs, selection, row spacing, grid contrast, zoom and playhead.
- [ ] 4.3 Keyframe interactions: multi-select, box select, move, copy and paste, keyboard navigation, context menus.
- [ ] 4.4 Playback: scrubbing, frame range display, onion-skin visibility.
- [ ] 4.5 Performance: measure painting on a large scene before and after.

## Acceptance criteria

- Existing scenes display correctly, and exposures stay exact.
- Keyframe edits are correct, and undo and redo work.
- The timeline stays responsive on large scenes. Performance is compared against a recorded baseline.

## Log

_No entries yet._
