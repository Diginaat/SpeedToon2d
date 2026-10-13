# Handoff

_Rewrite this file at the end of every session._

## Session 2026-10-13: Phase 0 foundation

**Requested:** Phase 0 only: inspect the repo, verify the toolchain, run a baseline build and launch, document the architecture, set up agent memory and the branch workflow, then commit and report.

**Completed**

- Confirmed that the repo is Tahoma2D (not OpenToonz) and that HEAD `3f2dde0af` equals `tahoma2d/tahoma2d` HEAD.
- Added remotes `upstream` (tahoma2d) and `opentoonz`. Created `dev/ui-modernization` and `feature/00-foundation`.
- Downloaded Qt 5.15.2 WinTab, Boost 1.87 and OpenCV 4.11 into the git-ignored `thirdparty/`.
- Configured with VS 18 and toolset v143, built RelWithDebInfo (exit 0) and launched the app (pass).
- Wrote AGENTS, CLAUDE, MEMORY, README, CONTRIBUTING and all of `docs/` (architecture, roadmap, build, testing, design-system stub, ADRs 0001-0002, phase files 00-08).
- Restored `LICENSE.txt` (BSD-3 requires it). Committed the owner's deletion of `AI_POLICY.md`, `CHANGELOG.md` and `.vscode/settings.json`.

**Incomplete**

- Baseline test scene (Phase 0 task 17). It needs the GUI.
- Manual regression checklist: only the launch step was run.

**Files modified:** `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `MEMORY.md`, `README.md`, `CONTRIBUTING.md`, `docs/**`. Deleted: `AI_POLICY.md`, `CHANGELOG.md`, `.vscode/settings.json`. **No source code changed.**

**Branch / commit:** `feature/00-foundation`. See `git log --oneline dev/ui-modernization..feature/00-foundation`. Nothing has been pushed.

**Commands executed:** see [BUILD-WINDOWS.md](../BUILD-WINDOWS.md). Configure, build, deploy and run were run exactly as written there.

**Build results:** exit 0, 0 errors, 1729 warnings (upstream noise).

**Tests:** automated none (no test infrastructure exists). Manual: app launch **pass**.

**Known issues:** see [phases/00-foundation.md](../phases/00-foundation.md#known-problems-found).

**Warnings for the next agent**

- Run the exe with its working directory set to `toonz/build/RelWithDebInfo`. Otherwise portable mode and `tahomastuff` are not found.
- In Git-Bash, never pass `-- /m` to `cmake --build` (MSYS path mangling).
- Use PowerShell for downloads, because Git-Bash `curl` is blocked here.
- Do not push or merge to `dev/ui-modernization` without owner approval.

**Exact next action:** the owner reviews the Phase 0 report and creates the test scene. Once Phase 1 is approved, merge `feature/00-foundation` into `dev/ui-modernization`, branch `feature/01-dark-ui`, and start task 1.1 (design tokens).
