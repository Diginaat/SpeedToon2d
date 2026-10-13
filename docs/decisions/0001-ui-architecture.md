# 0001 — UI architecture: extend the existing Qt 5 widgets

- **Status:** Accepted
- **Date:** 2026-10-13

## Context

The goal is a modern, Harmony-inspired UI on top of Tahoma2D.
The application is built on Qt 5.15 Widgets with:

- a custom docking framework (`toonzqt/docklayout`),
- LESS-generated QSS themes (`stuff/config/qss/Medium/less`),
- `QGraphicsView` schematics,
- a custom-painted Xsheet and Timeline (`toonz/xsheetviewer`).

See [ARCHITECTURE.md](../ARCHITECTURE.md).

## Problem

Should the modernization replace parts of the GUI stack, for example with Qt 6, QML, a web frontend or a third-party docking library? Or should it extend what exists?

## Alternatives considered

| Option | Why it was not chosen |
|---|---|
| Port to Qt 6 | Large mechanical port: QtScript was removed, and WinTab is supplied by a custom Qt 5.15.2 build. Unrelated to UX goals. |
| QML or web frontend | Would require rewriting every panel, and duplicates state and undo handling. |
| Qt Advanced Docking System | Would replace `DockLayout`, which room `.ini` persistence depends on. That breaks saved workspaces. |
| **Extend the existing widgets** | Selected. |

## Decision

- Stay on Qt 5.15.2 (the `tahoma2d/qt5` WinTab build) and C++17 as configured by upstream CMake.
- Theme work extends the existing LESS pipeline with new variables and theme files. It does not hard-code colours in C++.
- Workspace work adds new room presets under `stuff/profiles/layouts/rooms/`.
- Docking work modifies `DockLayout` and `TPanel` incrementally.
- Timeline, schematic and rigging work keep editing the real `TXsheet`, `TStageObjectTree` and `FxDag` data through `TUndo`.

## Compatibility implications

Scene files and the existing rooms and themes stay loadable. New presets are opt-in.

## Performance implications

None by default. Painting changes in Phase 4 and Phase 6 must be measured against the baseline.

## Risks and tradeoffs

- Qt 5.15 is end-of-life. A future Qt 6 port must be a separate ADR.
- The custom docking framework has less documentation than `QDockWidget`.

## Implementation references

`toonz/sources/toonzqt/docklayout.cpp`, `toonz/sources/toonz/mainwindow.cpp`, `toonz/sources/toonzlib/preferences.cpp`, `stuff/config/qss/Medium/less/`.
