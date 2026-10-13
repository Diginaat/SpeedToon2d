# Phase 5 — Layer hierarchy and folders

- **Status:** in progress (approved 2026-10-14). Phase 4 was paused to start it.
- **Branch:** `feature/05-layer-hierarchy`

## Goal

Make complex scenes easier to organise. Add a tree hierarchy with visibility and lock controls, search, and drag-and-drop.

## Where to start (verified paths)

- **Folder columns already exist in Tahoma2D:** `toonz/sources/include/toonz/txshfoldercolumn.h` and `toonz/sources/toonzlib/txshfoldercolumn.cpp`.
- Parenting: `TStageObjectTree` (`toonz/sources/toonzlib/tstageobjecttree.cpp`).
- Column types: `toonz/sources/toonzlib/txsh*column.cpp`.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 5.1 Document how columns, folder columns, stage-object parents, visibility and locks are represented.
- [ ] 5.2 Design the hierarchy UI. Reuse folder columns before inventing new scene data.
- [ ] 5.3 Integrate with the timeline, viewer, selection, undo and save/load.

## Acceptance criteria

- Hierarchies stay consistent. Grouping never changes animation silently.
- Drag-and-drop is predictable.
- Old files open. Any compatibility impact is documented in an ADR.

## Log

### Phase start
- Owner requested: commit and push Phase 4 work, then start Phase 5.
- Phase 4 was merged into `dev/ui-modernization` as paused, then this branch was cut from `dev/ui-modernization`.
- Start with task 5.1: document existing folder columns, column state, stage-object parenting, visibility and locks before changing UI or model code.
