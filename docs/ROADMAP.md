# Roadmap

The phases run in order. Each one needs explicit owner approval before it starts.
Status values are `not started`, `in progress`, `blocked` and `done`. Only use `done` after the phase's acceptance criteria have been verified.

| # | Phase | Branch | Status | Detail |
|---|---|---|---|---|
| 0 | Repository and development foundation | `feature/00-foundation` | done (test scene deferred) | [00-foundation](phases/00-foundation.md) |
| 1 | Modern dark UI, icons, typography | `feature/01-dark-ui` | in progress (1.1, 1.2 done) | [01-dark-ui](phases/01-dark-ui.md) |
| 2 | Harmony-inspired workspace preset | `feature/02-workspace` | not started | [02-workspace](phases/02-workspace.md) |
| 3 | Docking and panel management | `feature/03-docking` | not started | [03-docking](phases/03-docking.md) |
| 4 | Horizontal timeline and keyframes | `feature/04-timeline` | not started | [04-timeline](phases/04-timeline.md) |
| 5 | Layer hierarchy and folders | `feature/05-layer-hierarchy` | not started | [05-layer-hierarchy](phases/05-layer-hierarchy.md) |
| 6 | Node editor redesign | `feature/06-node-editor` | not started | [06-node-editor](phases/06-node-editor.md) |
| 7 | Puppet rigging workflow | `feature/07-puppet-rigging` | not started | [07-puppet-rigging](phases/07-puppet-rigging.md) |
| 8 | Advanced deformers | `feature/08-deformers` | not started | [08-deformers](phases/08-deformers.md) |

## Principles

- Ship one small, verified task per commit. Never start a later phase early.
- UI phases (1-3) must not change the scene file format.
- Phases 4-8 may touch `toonzlib/` and `tnzext/`. Any format change needs an ADR in [decisions/](decisions/).
- Each phase file holds its own task checklist. This table only tracks status.

## Branch strategy

See [ADR 0002](decisions/0002-branch-and-upstream-strategy.md).

```
master                    mirrors upstream tahoma2d/tahoma2d; never commit fork work here
dev/ui-modernization      integration branch; phases merge here after verification
feature/NN-<name>         one branch per phase, cut from dev/ui-modernization
```
