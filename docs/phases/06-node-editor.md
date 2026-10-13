# Phase 6 — Node editor redesign

- **Status:** not started. This phase needs owner approval before it begins.
- **Branch:** `feature/06-node-editor`

## Goal

Make the stage and FX schematics clearer and faster to use. They must keep editing the real scene data.

## Where to start (verified paths)

- `SchematicViewer`, `SchematicNode` and `SchematicPort`: `toonz/sources/include/toonzqt/schematicviewer.h` and `toonz/sources/toonzqt/schematicnode.cpp`.
- `toonz/sources/toonzqt/stageschematic*.cpp`, `fxschematic*.cpp` and `schematicgroupeditor.cpp`.
- Models: `TStageObjectTree` and `FxDag` (`toonz/sources/include/toonz/fxdag.h`).

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 6.1 Document the scene, node and link classes and how they sync with the model.
- [ ] 6.2 Node visuals: ports, labels, links, selected and hover states, spacing.
- [ ] 6.3 Navigation: pan, zoom, fit, frame selected, multi-select, node search.
- [ ] 6.4 Organisation: groups, backdrops and notes, alignment, link routing.

## Acceptance criteria

- Existing graphs display the same, and connections keep their meaning.
- Undo and redo work. Large graphs stay interactive.
- Rendered output is unchanged.

## Log

_No entries yet._
