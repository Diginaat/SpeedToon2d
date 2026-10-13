# Phase 8 — Advanced deformers

- **Status:** not started. This phase needs owner approval before it begins.
- **Branch:** `feature/08-deformers`

## Goal

Extend deformation capabilities after an architecture study. Add one deformer at a time.

## Where to start (verified paths)

- Existing plastic mesh deformation: `toonz/sources/tnzext/plasticdeformer.cpp` and `plasticskeletondeformation.cpp`.
- Render integration: `toonz/sources/toonzlib/plasticdeformerfx.cpp`.
- Stroke deformation: `toonz/sources/tnzext/StrokeDeformation*.cpp`.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [ ] 8.1 Research which deformers already exist and which are missing (mesh, skeletal, curve, envelope, lattice, weights).
- [ ] 8.2 Write an architecture proposal as an ADR: data, channels, rendering, CPU or GPU, undo, serialisation, compatibility.
- [ ] 8.3 Prototype the simplest valuable missing deformer.
- [ ] 8.4 Profile it. Avoid allocations during interaction.
- [ ] 8.5 Integrate with the hierarchy, timeline, properties, viewer, save/load and undo.
- [ ] 8.6 Add further deformers one at a time, each with its own tests and docs.

## Acceptance criteria

- Deformation results are predictable and animation is stable.
- Interactive performance is acceptable, and results are compared with the baseline.
- Save and load work, and undo works. No existing scene is corrupted.

## Log

_No entries yet._
