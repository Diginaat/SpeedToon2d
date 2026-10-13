# AGENTS.md — start here

This is the entry point for every AI coding agent and every new human contributor.
Read it fully before you change anything.

## Mission

SpeedToon2d is a fork of **Tahoma2D** (and so of OpenToonz). It is being modernised into a Toon Boom Harmony-inspired 2D animation tool.
The work improves usability (theme, workspace, docking, timeline, hierarchy, node editor, rigging, deformers) and keeps existing scenes compatible.
Take inspiration from proprietary software, but never copy its code, icons, artwork or trademarks.

## Required reading order

1. `AGENTS.md` (this file)
2. [`MEMORY.md`](MEMORY.md): current state and next actions
3. [`docs/ROADMAP.md`](docs/ROADMAP.md): phase status
4. [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md): where the code is
5. [`docs/agents/HANDOFF.md`](docs/agents/HANDOFF.md): what the last session left
6. `docs/phases/NN-*.md` for your assigned phase

Then run `git status`, `git branch --show-current` and `git log --oneline -10`.

## Workflow (one small task at a time)

1. Research the code. Search for an existing implementation before you add a new system.
2. Write the plan and the task list in the phase file.
3. Implement **one** task.
4. Build: `cmake --build toonz/build --config RelWithDebInfo --parallel` (see [docs/BUILD-WINDOWS.md](docs/BUILD-WINDOWS.md)).
5. Test using [docs/TESTING.md](docs/TESTING.md). A successful compile alone does not count as verified.
6. Review your own diff.
7. Update the phase file, `MEMORY.md` and `docs/agents/HANDOFF.md`.
8. Commit, then move to the next task.

Never start the next **phase** without the owner's approval. End each phase with the report template in [docs/phases/00-foundation.md](docs/phases/00-foundation.md#phase-report-template).

## Architectural boundaries

- Stay on Qt 5.15 Widgets and C++. Do not add Qt 6, QML, web or Electron without an ADR and owner approval ([ADR 0001](docs/decisions/0001-ui-architecture.md)).
- UI phases (1-3) touch only `toonz/sources/toonz/`, `toonz/sources/toonzqt/` and `stuff/`. They must not change the scene format.
- Changes to `toonzlib/`, `tnzext/` or `tnzcore/`, and any file-format change, need an ADR in `docs/decisions/`.
- Every edit to scene data goes through a `TUndo` subclass. Widgets never mutate the model directly.
- Style through LESS and QSS (`stuff/config/qss/Medium/less/`). Do not hard-code colours in C++.
- No new third-party dependency without documenting its licence, maintenance status, size and alternatives.

## Coding standards

- Follow the surrounding code: Qt naming, `m_` members, 2-space indent. Format with `toonz/sources/.clang-format`, and only the lines you changed.
- Use small classes with clear names. Keep logic out of paint and event handlers where practical.
- Keep Qt parent/child ownership. Do not use raw `new` without a parent or a smart pointer.
- Add short comments only where behaviour is non-obvious.

## Git conventions

- Remotes and branches: see [ADR 0002](docs/decisions/0002-branch-and-upstream-strategy.md). Never commit to `master`.
- Work on `feature/NN-<name>`, which is cut from `dev/ui-modernization`. Parallel agents use `git worktree`.
- Use Conventional Commits, for example `feat(timeline): ...`, `fix(docking): ...` or `docs: ...`. Each commit holds one logical change.
- Never force-push, rewrite pushed history or push without owner approval.
- Never commit `toonz/build/`, `thirdparty/{qt,boost,opencv}/`, caches, credentials or machine-specific paths.

## Memory rules

- The repository is the shared memory. Conversation history is not.
- `MEMORY.md` stays concise and factual. Update it whenever the state changes, and keep commit hashes accurate.
- Never record a test result you did not observe. Use **not run** where that applies.
- `docs/agents/HANDOFF.md` is rewritten at the end of every session.

## Safe collaboration

- Check HANDOFF and recent commits for work that touches the same files. If you find any, coordinate through the docs before editing.
- Stay in your assigned scope. Do not reformat or refactor unrelated code.
- If you don't understand someone else's code, read it and its docs. Do not guess.
