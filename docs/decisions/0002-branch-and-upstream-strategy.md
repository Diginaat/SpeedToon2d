# 0002 — Branch and upstream strategy

- **Status:** Accepted
- **Date:** 2026-10-13

## Context

This repository (`Diginaat/SpeedToon2d`) is a fork of **Tahoma2D**, which is itself a fork of OpenToonz.
At fork time, `master` was identical to `tahoma2d/tahoma2d` HEAD (`3f2dde0af`).

Tahoma2D's `AI_POLICY.md` states that PRs containing significant AI-generated code are closed without review.
The owner removed that file, together with Tahoma2D's restrictive `AGENTS.md` and `CLAUDE.md`, from this fork.
This project is developed with AI agents, so its work is not expected to be accepted upstream.

## Problem

The project needs a remote and branch layout that does three things:

- Tracks Tahoma2D for bug fixes.
- Allows reference to OpenToonz.
- Keeps unfinished fork work away from the upstream mirror.

## Alternatives considered

1. Track `opentoonz/opentoonz` as `upstream`. This was rejected because the history is Tahoma2D's, so merges would be painful.
2. Track only `tahoma2d/tahoma2d`. This works, but OpenToonz fixes can then only be reached indirectly.
3. **Track `tahoma2d/tahoma2d` as `upstream` and add `opentoonz/opentoonz` as the reference remote `opentoonz`.** This was selected.

## Decision

| Remote | URL | Use |
|---|---|---|
| `origin` | `https://github.com/Diginaat/SpeedToon2d.git` | The project fork. Push here. |
| `upstream` | `https://github.com/tahoma2d/tahoma2d.git` | Pull fixes into `master`. |
| `opentoonz` | `https://github.com/opentoonz/opentoonz.git` | Read and cherry-pick reference only. |

Branches:

- `master` is a mirror of `upstream/master`. Only fast-forward it, and never commit fork work to it.
- `dev/ui-modernization` is the integration branch. A phase merges into it only after its acceptance criteria pass.
- `feature/NN-<name>` holds one branch per phase, cut from `dev/ui-modernization`.
- Parallel agents use `git worktree` for isolation.
- Never force-push or rewrite pushed history without owner approval.

## Consequences

- To sync upstream, run `git fetch upstream`, fast-forward `master`, then merge `master` into `dev/ui-modernization`.
- The OpenToonz and Tahoma2D histories have diverged since 2020. Cherry-picks from `opentoonz` often need manual porting.
- Upstream PRs are out of scope. Fork-specific files (this `docs/` folder, `AGENTS.md`, `MEMORY.md`) never go upstream.
- Licence: Tahoma2D is BSD-3-Clause (`LICENSE.txt`). Keep that file and its notice intact.
