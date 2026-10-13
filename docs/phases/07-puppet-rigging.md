# Phase 7 — Puppet rigging workflow

- **Status:** not started. This phase needs owner approval before it begins.
- **Branch:** `feature/07-puppet-rigging`

## Goal

Improve how cut-out rigs are built and posed, using the existing Skeleton, Plastic and IK systems first.

## Where to start (verified paths)

- Skeleton tool: `toonz/sources/tnztools/skeletontool.{h,cpp}` and `skeletonsubtools.cpp`.
- IK: `toonz/sources/toonzlib/{ikengine,ikjacobian,iknode,ikskeleton,skeleton}.cpp`.
- Plastic: `toonz/sources/tnzext/plastic*.cpp` and `toonz/sources/tnztools/plastictool*.cpp`.
- Hooks: `toonz/sources/tnztools/hooktool.cpp`.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 7.1 Audit parenting, pivots, transform channels, IK, plastic and interpolation. Record the findings here.
- [ ] 7.2 Rig hierarchy UX: visualisation, selection, pivot editing, transform handles.
- [ ] 7.3 Animation controls: keying transforms and switching between pose and edit modes.
- [ ] 7.4 Expose the existing IK. Design FK/IK switching as a separate task.
- [ ] 7.5 Build a test character (torso, head, upper arms, forearms, hands, upper legs, lower legs, feet) under `test-scenes/`.

## Acceptance criteria

- The test character can be rigged, posed, animated, saved and reloaded.
- Undo and redo work. Existing rigs behave the same.

## Log

_No entries yet._
