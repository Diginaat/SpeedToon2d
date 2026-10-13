# Phase 0 — Repository and development foundation

- **Status:** in progress. Everything is done except the baseline test scene (task 17).
- **Branch:** `feature/00-foundation` (cut from `dev/ui-modernization`, which was cut from `master` @ `3f2dde0af`)

## Goal

Establish a verified build, a documented architecture and agent memory before any UI work starts.

## Tasks

- [x] 1-2. Inspect the repository. HEAD is `3f2dde0af`, identical to `tahoma2d/tahoma2d` HEAD on 2026-10-13. The app is Tahoma2D 1.6.3.
- [x] 3-4. Build system and toolchain. See [BUILD-WINDOWS.md](../BUILD-WINDOWS.md).
- [x] 5. Git LFS: installed (3.7.1) but **not used** by the repo (`git lfs ls-files` is empty).
- [x] 6. Build the unmodified app: exit 0, 0 errors, 1729 warnings.
- [x] 7. Launch: main window opens and is responsive ([screenshot](img/00-baseline-launch.png)).
- [x] 8. Record warnings and errors. See BUILD-WINDOWS §4 and *Known problems* below.
- [x] 9. Identify source areas. See [ARCHITECTURE.md](../ARCHITECTURE.md).
- [x] 10-15. Docs structure, AGENTS.md, MEMORY.md, HANDOFF.md, ARCHITECTURE.md, ROADMAP.md.
- [x] 16. Branch strategy. See [ADR 0002](../decisions/0002-branch-and-upstream-strategy.md). Remotes `upstream` and `opentoonz` were added.
- [ ] 17. **Baseline test scene.** Not created, because building it needs GUI interaction. The spec is in [TESTING.md](../TESTING.md#baseline-test-scene).
- [x] 18. Baseline commit recorded in `MEMORY.md`.

## Acceptance criteria

| Criterion | Result |
|---|---|
| Baseline build verified | **pass**: `cmake --build toonz/build --config RelWithDebInfo --parallel`, exit 0 |
| Application launches | **pass**: window "Tahoma2D 1.6.3", responsive after 25 s |
| Build instructions reproducible | **pass**: commands in BUILD-WINDOWS were run as written. Download commands were run from an equivalent script. |
| Documentation navigable | **pass**: [docs/README.md](../README.md) index |
| Agent memory initialised | **pass** |
| Git working tree clean | **pass** after the Phase 0 commits |
| Existing problems documented | **pass** |
| Baseline test scene | **not done** |

## Known problems found

- CMake 4.x needs `-DCMAKE_POLICY_VERSION_MINIMUM=3.5`, because upstream declares `cmake_minimum_required(VERSION 2.8.11)`.
- In this environment, Git-Bash `curl` cannot reach GitHub, while PowerShell `Invoke-WebRequest` can.
- `doc/how_to_stylesheet.md` refers to `stuff/config/qss/Default/less`. The actual path is `Medium/less`.
- The owner removed `.vscode/settings.json`. `doc/how_to_stylesheet.md` expected it for LESS compile settings, so recreate it locally if needed.
- There are no automated tests upstream.
- `ffmpeg` and `rhubarb` are not deployed, so video I/O and lip-sync are untested.
- The manual regression checklist in TESTING.md has **not** been run yet, beyond launching the app.

## Phase report template

```
## Phase completion report
Phase: / Status: Completed | Partially completed | Blocked
Implemented / Files changed / Technical decisions / Validation (exact commands + results) /
Performance / Compatibility / Git (branch, commits) / Remaining issues / Documentation / Next phase
```
