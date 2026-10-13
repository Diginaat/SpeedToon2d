# Testing

## Current state

The upstream tree has **no automated tests**: no test target exists in any `CMakeLists.txt`.
For now, verification means a successful build plus the manual checklist below.
Never mark a feature as verified from compilation alone.

## Build check

```sh
cmake --build toonz/build --config RelWithDebInfo --parallel
```

The build must end with `exit 0`. Record any new warnings in the files you changed.

## Manual regression checklist

Run this in the built app (see [BUILD-WINDOWS.md](BUILD-WINDOWS.md#run)).
Use a **copy** of the test scene, never the original.

| # | Check | Expected result |
|---|---|---|
| 1 | Start the app | Main window opens with no error dialogs |
| 2 | Open `test-scenes/baseline` (see below) | Scene loads, viewer shows frame 1 |
| 3 | Step frames with `.` and `,`, then play | Viewer updates and playback loops |
| 4 | Switch rooms (tabs on top) | Every room renders, panels are not blank |
| 5 | Preferences > Interface > Theme: switch through all themes | Text and icons stay readable |
| 6 | Timeline: select cells, drag them, then undo and redo | Cells move back and forth correctly |
| 7 | Set a position keyframe, then undo and redo | Keyframe icon appears, disappears and reappears |
| 8 | Schematic: toggle stage and FX, drag a node, undo | Node returns to its position |
| 9 | Save As to a temp folder, close, reopen | Scene is identical |
| 10 | Quit and restart | Room layout is restored |

Record results in the phase file and in `MEMORY.md`. Use **pass**, **fail** or **not run**, and give the commit hash.

## Baseline test scene

Status: **not yet created.** It must be built in the GUI, because hand-writing `.tnz` XML risks producing an invalid file.
Specification for the first person or agent with GUI access:

- Location: `test-scenes/baseline/` (a Tahoma2D project folder).
- Camera 1920x1080, 24 fps, 48 frames.
- Column 1: a vector level with 4 drawings, exposed on twos.
- Column 2: a raster level with 2 drawings.
- Column 3: a pegbar parent of column 1, with 3 position keyframes.
- One FX (Blur) on column 2.
- Keep the total size under 1 MB.

## Planned automation

Phase 0 follow-up. Add a minimal QtTest target for `toonzlib`-level logic (xsheet cell ops, keyframes, scene save and load round-trips). Add it as its own CMake option so it does not affect the default build.
