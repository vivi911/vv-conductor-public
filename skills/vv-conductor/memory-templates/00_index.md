# 00 Index

This file answers exactly one question: where should the AI go to read your background and your projects.

## Fixed entry points

| Type | File | Purpose |
|---|---|---|
| Who I am | `01_who-i-am.md` | Identity, working style, preferences, no-go zones |
| Projects | `projects/<project-name>.md` (one file per project, copied from `02_project-template.md` — see "Current key projects" below) | Where each project stands, what's blocking it, next step |
| Work rules | `03_ai-work-rules.md` | Rules the AI must follow before starting work |
| Conductor | the installed `vv-conductor` skill | Task tiers, dispatch, red/yellow/green authorization, verification |
| Boss View | the installed `vv-conductor` skill | Helps you decide what to prioritize today |

The first three are **yours** — they live in your Vault (default `~/vv-memory/`) and you fill them in. The last two are vv's own rules, already built into the skill — you don't need to prepare anything extra for those.

## Current key projects

List your active projects here:

One file per project, stored in `~/vv-memory/projects/`. Add a row here whenever you add a new one.

| Project | File | Next step | Status |
|---|---|---|---|
| TBD | `projects/TBD.md` | TBD | In progress |

## AI kickoff rules

At the start of every new conversation, the AI must read, in order:

1. This file.
2. `01_who-i-am.md`.
3. The project file or handoff relevant to this task.
4. `03_ai-work-rules.md`.

After reading, the first line back should be a "memory signal."
