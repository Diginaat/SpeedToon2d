# Architecture

How the SpeedToon2d source tree is organised, and where each modernization phase will touch it.
Every path is relative to the repository root and was checked against commit `3f2dde0af`, the Tahoma2D upstream HEAD.

> SpeedToon2d is a fork of **Tahoma2D** (version 1.6). Tahoma2D is itself a fork of **OpenToonz**.
> Most OpenToonz documentation still applies, but class names, folder names (`tahomastuff`) and
> some features (folder columns, the Medium LESS theme) are Tahoma2D-specific.

## 1. Top-level layout

| Path | Purpose |
|---|---|
| `toonz/sources/` | All C++ sources. The CMake entry point is `toonz/sources/CMakeLists.txt`. |
| `toonz/build/` | Local build output (git-ignored, see [BUILD-WINDOWS.md](BUILD-WINDOWS.md)). |
| `stuff/` | Runtime data: themes, room layouts, shortcuts, presets and the library. At runtime it is copied next to the executable as `tahomastuff/`. |
| `thirdparty/` | Bundled libraries (tiff, png, glew, mypaint, ...). Qt, Boost and OpenCV are downloaded here locally and git-ignored. |
| `ci-scripts/` | CI build scripts per platform. `ci-scripts/windows/*.bat` is the reference for the Windows build. |
| `doc/` | Upstream developer docs (build, stylesheets, rendering overview). |
| `docs/` | **This project's** documentation and agent memory. |

## 2. Library layering (`toonz/sources/`)

Libraries build in this order (`toonz/sources/CMakeLists.txt` lines 698-716). Each one depends only on the ones listed before it.

```
tnzcore   geometry, images, params, undo (TUndo), smart pointers
tnzbase   FX/param base, tfx, rendering primitives
tnzext    plastic (mesh) deformation, stroke deformation
toonzlib  SCENE MODEL: xsheet, columns, levels, stage objects, IK, preferences
stdfx     standard FX plugins
toonzqt   REUSABLE QT WIDGETS: docking, schematic, function editor, dvwidgets
tnztools  viewer tools: brush, skeleton, plastic, animate, hook...
toonz     THE APPLICATION: main window, rooms, panels, xsheet/timeline viewer, scene viewer
```

**Boundary rule.** UI-only work (Phases 1-3) should stay in `toonz/`, `toonzqt/` and `stuff/`.
Changes to `toonzlib/` or `tnzext/` change the scene model or the file format. They need an ADR.

## 3. Feature areas

### 3.1 Themes and stylesheets (Phase 1)

- The LESS source is in `stuff/config/qss/Medium/less/`. `main.less` imports `base/`, `components/`, `layouts/` and `tahoma/`.
- The theme variants are `stuff/config/qss/Medium/less/themes/{Dark,Darker,Light,Neutral}.less`. Each one overrides `@bg`, `@accent` and similar variables and writes its output to `stuff/config/qss/<Name>/<Name>.qss` (see the `// out:` header).
- Generated QSS lives in `stuff/config/qss/{Medium,Dark,Darker,Light,Neutral}/`.
- Loader: `Preferences::getCurrentStyleSheet()` in `toonz/sources/toonzlib/preferences.cpp` (around line 1066). It resolves `<configDir>/qss/<Name>/<Name>.qss`.
- Icons are in `stuff/config/qss/Medium/imgs/` (white and black variants).
- Hard-coded colours also exist in C++ as Q_PROPERTYs that the QSS sets, for example in `toonz/sources/toonz/xsheetviewer.h`. Audit them in Phase 1.
- Note: `doc/how_to_stylesheet.md` refers to `Default/less`, but the real folder is `Medium/less`.

### 3.2 Rooms and workspaces (Phase 2)

- A room is a tab of docked panels. Class `Room` (derived from `TMainWindow`) is in `toonz/sources/toonz/mainwindow.h:26`. Save and load are in `mainwindow.cpp` (`Room::save` at line 253, `Room::reload` at 374, `MainWindow::readSettings` at 615, `MainWindow::writeSettings` at 712).
- Room presets are `stuff/profiles/layouts/rooms/<Preset>/room*.ini` plus `layouts.txt`. The available presets are `Default`, `OpenToonz` and `StudioGhibli`.
- Each `roomN.ini` stores `pane_N\name` (a panel factory id), `geometry` and a `hierarchy=` string that encodes the dock tree.
- Panel ids are registered with `TPanelFactory("<Id>")` in `toonz/sources/toonz/tpanels.cpp`, for example `Xsheet`, `Timeline`, `Schematic`, `SceneViewer`, `ToolBar`, `ToolOptions` and `FunctionEditor`.

### 3.3 Docking and panels (Phase 3)

- The docking framework is custom and does **not** use `QDockWidget`. It lives in `toonz/sources/toonzqt/docklayout.{h,cpp}` (`DockLayout`, `DockWidget`, `DockPlaceholder`, `DockSeparator`, `Region`).
- `toonz/sources/toonzqt/tdockwindows.{h,cpp}` holds `TMainWindow` and `TDockWidget`, which are the app-level wrappers.
- `toonz/sources/toonz/pane.{h,cpp}` holds `TPanel` (derived from `TDockWidget`) and `TPanelTitleBar` with its title-bar buttons.
- Floating panels: `toonz/sources/toonz/floatingpanelcommand.cpp`.

### 3.4 Xsheet and Timeline (Phase 4)

- The Xsheet and the Timeline are **the same widget** in two orientations. `XsheetViewer` is in `toonz/sources/toonz/xsheetviewer.{h,cpp}`.
- The orientation abstraction is in `toonz/sources/include/orientation.h` and `toonz/sources/toonzlib/orientation.cpp`. The `Orientation` and `Orientations` classes have top-to-bottom (Xsheet) and left-to-right (Timeline) variants.
- Areas: `xshcellviewer` (cells, `CellArea`), `xshcolumnviewer` (column and layer headers), `xshrowviewer` (frame ruler), `layerheaderpanel`, `layerfooterpanel`, `xshnoteviewer` and `frameheadgadget` (playhead).
- Drawing **exposures** are `TXshCell` entries in `TXshColumn`s (`toonz/sources/toonzlib/txshcell.cpp`, `txshcolumn.cpp`, `txsheet.cpp`).
- Property **keyframes** are `TDoubleParam` keyframes on `TStageObject` channels (`toonz/sources/include/tdoubleparam.h`, `toonz/sources/toonzlib/tstageobject.cpp`). Their UI is `keyframeselection`, `keyframemover`, `cellkeyframeselection` (in `toonz/`) and the Function Editor (`toonz/sources/toonzqt/function*.cpp`).
- Cell drag, move and commands: `xshcellmover.cpp`, `xsheetdragtool.cpp`, `xsheetcmd.cpp`, `cellselection.cpp`.

### 3.5 Columns, hierarchy and folders (Phase 5)

- Column types are in `toonz/sources/toonzlib/txsh*column.cpp` (level, mesh, palette, sound, sound-text, zerary FX, pegbar, **folder**).
- **Tahoma2D already has folder columns.** See `toonz/sources/include/toonz/txshfoldercolumn.h` and `toonz/sources/toonzlib/txshfoldercolumn.cpp`. Phase 5 must start from these.
- Stage-object parenting uses `TStageObjectTree` (`toonz/sources/toonzlib/tstageobjecttree.cpp`) and `TStageObject::setParent`.

### 3.6 Schematic / node editor (Phase 6)

- The generic graph view is `SchematicViewer`, `SchematicNode` and `SchematicPort`, in `toonz/sources/include/toonzqt/schematicviewer.h` and `toonz/sources/toonzqt/schematicnode.cpp`. It is built on `QGraphicsScene` and `QGraphicsView`.
- The stage graph (pegbars, columns, cameras) is in `toonz/sources/toonzqt/stageschematic*.cpp`.
- The FX graph is in `toonz/sources/toonzqt/fxschematic*.cpp`. Node groups: `schematicgroupeditor.cpp`.
- The nodes edit real `TStageObjectTree` and `FxDag` data. There is no separate graph model.

### 3.7 Rigging and deformation (Phases 7-8)

- Skeleton tool and IK: `toonz/sources/tnztools/skeletontool.{h,cpp}`, `skeletonsubtools.cpp` and `toonz/sources/toonzlib/{ikengine,ikjacobian,iknode,ikskeleton,skeleton}.cpp`.
- Plastic (mesh) deformation:
  - Model: `toonz/sources/tnzext/plastic*.cpp` and `meshbuilder.cpp`.
  - Tool: `toonz/sources/tnztools/plastictool*.cpp`.
  - Render FX: `toonz/sources/toonzlib/plasticdeformerfx.cpp`.
  - Mesh column: `txshmeshcolumn.cpp`.
- Hooks (pivot and attachment points): `toonz/sources/tnztools/hooktool.cpp` and `hookselection.cpp`.

## 4. Undo and redo

All edits go through `TUndo` subclasses that are registered with `TUndoManager` (`toonz/sources/include/tundo.h`). Every new interaction must push an undo object. Never mutate scene data directly from a widget.

## 5. Tests

The upstream tree has **no automated test target**. No GoogleTest, QtTest or `add_test` exists in any `CMakeLists.txt`. [TESTING.md](TESTING.md) describes the manual regression procedure and the plan for adding tests.
