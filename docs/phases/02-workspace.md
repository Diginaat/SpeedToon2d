# Phase 2 — Harmony-inspired workspace preset

- **Status:** done (approved 2026-10-13). Phase 1 was paused to start it.
- **Branch:** `feature/02-workspace`

## Goal

Add an opt-in animation room preset: viewer in the centre, tools on the left, timeline and layers at the bottom, properties on the right, and the node editor one click away.

## Where to start (verified paths)

- Room presets: `stuff/profiles/layouts/rooms/{Default,OpenToonz,StudioGhibli}/` (`layouts.txt` plus `roomN.ini`).
- `Room` and `MainWindow::readSettings`/`writeSettings`: `toonz/sources/toonz/mainwindow.{h,cpp}`.
- Panel ids: `TPanelFactory("...")` in `toonz/sources/toonz/tpanels.cpp`.

## Tasks

Split each task into commits small enough to build and test on their own. Tick a task only after it has been verified.

- [x] 2.1 Document how rooms, `layouts.txt` and the `hierarchy=` dock-tree encoding work.
- [x] 2.2 Add a new preset folder with the modern layout.
- [x] 2.3 Let users switch between the original and modern layouts.
- [x] 2.4 Verify that the layout persists across restarts using the existing settings.

## Acceptance criteria

- The workspace opens correctly and is restored after a restart.
- Existing presets still work. Scene data does not change.

## Log

### 2.1 How rooms work
- **Presets:** each preset is a folder `stuff/profiles/layouts/rooms/<Preset>/` containing `layouts.txt` (the ordered room files) and `roomN.ini`.
- **Selection:** the *Preferences > Interface > Rooms\** setting stores `CurrentRoomChoice` and applies after a restart. The list is a folder scan in the `Preferences` constructor (`toonz/sources/toonzlib/preferences.cpp`, around line 360).
- **First run:** `MainWindow::readSettings` loads the template. `makePrivate` and `writeRoomList` then copy the rooms to `profiles/users/<user>/layouts/<Preset>/`, which `ToonzFolder::getRoomsFile` prefers from then on. `currentRoom.txt` stores the active tab.
- **`roomN.ini` format:**
  - `[room]` contains `pane_N
ame` (a `TPanelFactory` id from `tpanels.cpp`), `pane_N\geometry=@Rect(x y w h)`, plus each panel's own keys (`SaveLoadQSettings`), and finally `name=`.
  - `hierarchy="<max> <orient> <tree>"`, written by `DockLayout::saveState` and read by `restoreState` (`toonz/sources/toonzqt/docklayout.cpp`, around line 1368).
    - `<max>` is the maximised pane index, or `-1`.
    - `<orient>` is the root orientation: `0` puts children side by side, `1` stacks them top to bottom. Each nesting level alternates.
    - `[ … ]` groups regions, and a number is a pane index.
    - Panes that are not in the tree are floating.
  - Region sizes are derived from the pane rects (`Region::restoreGeometry`), so the rects must tile exactly. The Default presets use a 1920x1097 room with 4 px separators. `redistribute()` fits the result to the real window.
- **Limitation:** panels cannot be tabbed together, because the dock framework has no tab docking. "Easy access" to the node editor therefore means giving it its own dock area.

### 2.2 Modern preset with an Animation room
- `stuff/profiles/layouts/rooms/Modern/` is a copy of `Default`, so StopMotion, Timing, FX, Browser and History are unchanged. `room1.ini` is replaced with the new **Animation** room:

  ```
  ToolOptions (full width)
  ToolBar | SceneViewer                     | StyleEditor
          |                                 | LevelPalette
          | Timeline                | Schematic (Stage view)
  ```

  `hierarchy="-1 1 [ 0 [ 1 [ [ 2 [ 3 4 ] ] [ 5 6 ] ] ] ] "`. The Schematic uses `viewtype=1`, the stage, pegbar and rig graph. Pane settings are copied from Default `room1.ini`.
- No C++ changed and no scene data changed: rooms are separate files from scenes.

### 2.3 Switching
Already provided. *Preferences > Interface > Rooms* now lists `Modern` next to `Default`, `OpenToonz` and `StudioGhibli`, and the existing presets are untouched.

### 2.4 Persistence (tested at 1.0 scale only, as the owner asked)
- With `CurrentRoomChoice=Modern`, the app launched with the **Animation** tab active ([img](img/02-animation-room.png)).
- On launch, the private copy was created in `profiles/users/<user>/layouts/Modern/`.
- The app quit normally (exit within 15 s). `room1.ini` had been rewritten with the same hierarchy, and `currentRoom.txt` = `Animation`.
- After a relaunch, the same layout was restored.
- **Not tested:** switching through the Preferences dialog (only the ini value was set), and a user-modified layout surviving a restart.

### Notes
- `Default` stays the default preset for new users. Making `Modern` the default is a one-line change (`define(CurrentRoomChoice, …, "Default")` in `preferences.cpp`) and waits for the owner's decision.
