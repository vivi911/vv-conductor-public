# 02 Project Template

This is a **blank master** — don't fill it in directly here.

## How to save your first project

Copy this into your Vault, and name the file after the project:

```bash
mkdir -p ~/vv-memory/projects
cp -n ~/vv-memory/02_project-template.md ~/vv-memory/projects/my-first-project.md
```

## How to save your second, third project, and so on

**One project, one file — never overwrite the previous one.** Just copy again with a new filename:

```bash
cp -n ~/vv-memory/02_project-template.md ~/vv-memory/projects/another-project.md
```

Use any short name you'll recognize — doesn't have to be in English. Every time you add one, remember to add a row in `00_index.md`'s project table, so vv can find it.

When vv saves on your behalf, it follows the same rule: **new project, new file — never overwrite an existing project file.**

## Project name

TBD.

## What problem this project solves

TBD.

State it plainly in one sentence:

```text
This project exists so that [who], in [what situation], can skip [what hassle] and get [what result].
```

## Where it stands right now

TBD.

Write the actual concrete state — not just "in progress."

## Current blockers

TBD.

Blockers come in three kinds:

- Decision blocked: needs someone to sign off.
- Data blocked: missing data, permissions, or a source.
- Build blocked: a technical or execution problem.

## Top 3 recommended next steps

1. TBD.
2. TBD.
3. TBD.

## What needs my sign-off

TBD.

## Off-limits areas

TBD.

For example:

- Don't touch real/live members.
- Don't send external notifications.
- Don't switch production traffic over.
- Don't delete data.

## Sources of truth

| Type | Path or link |
|---|---|
| Latest handoff | TBD |
| Rules document | TBD |
| Primary data | TBD |
| Deliverable | TBD |

## Kickoff prompt for the AI

```text
Please read this project summary first, then read the sources of truth.
Report back first: where things stand, current blockers, recommended next step.
Never claim something is done without evidence.
```
