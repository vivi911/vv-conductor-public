# skill-index

This file is the skill entry-point index for the "AI Co-Pilot Coach" public package. The technical name stays `vv-conductor`, so existing install and trigger mechanics keep working.

## Current official skill

| Skill | Path | Purpose |
|---|---|---|
| vv-conductor | `skills/vv-conductor/SKILL.md` | Has Codex / Claude Code walk a beginner through safely finishing their first task, then bring in memory, dispatch, red/yellow/green authorization, verification, and handoff |

## What triggers it

`vv-conductor` should be used whenever the user says any of the following:

- `vv`
- `vivi`
- `AI co-pilot coach`
- `co-pilot coach`
- `kickoff playbook`
- `conductor`
- `dispatch`
- `what should I do today`
- `I'm feeling overwhelmed`
- `help me prioritize`
- `red/yellow/green`
- `handoff`
- `memory templates`
- `use the vv v1.6 workflow`

## How to install it

Both Codex and Claude Code can install the same `skills/vv-conductor/` folder. Only the target directory differs.

Codex:

```bash
mkdir -p ~/.codex/skills
cp -R ~/vv-conductor-public/skills/vv-conductor ~/.codex/skills/vv-conductor
```

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R ~/vv-conductor-public/skills/vv-conductor ~/.claude/skills/vv-conductor
```

After restarting, `vv-conductor` becomes a triggerable skill. Installing both at once won't cause any conflict.

**Traditional Chinese version**: the same package also ships in Traditional Chinese under [`zh-TW/`](zh-TW/skill-index.md) (`zh-TW/skills/vv-conductor/`). Both language packages install to the same target folder name (`~/.claude/skills/vv-conductor/` or `~/.codex/skills/vv-conductor/`) — pick the one you want; installing both at once means whichever you copy second overwrites the first.

If the AI tool you're using doesn't have a skill-directory mechanism, the fallback is: drop `SKILL.md` and everything under `references/` into that tool's rules or project-knowledge area, and ask it to read them at the start of the conversation.

## Maintenance rules

- Keep `SKILL.md` short — only triggers, flow, and the judgment calls that actually matter.
- Detailed rules live in `references/`.
- Run the validator after editing `SKILL.md`.
- Scan for sensitive information before sharing publicly.
