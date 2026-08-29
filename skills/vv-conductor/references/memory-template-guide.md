# Memory Template Guide

Use this reference when the user wants vv (vv-pack-1.7.0) to remember who they are, what projects are running, or what AI should never do.

## Required Files

```text
memory-templates/
├── 00_index.md
├── 01_who-i-am.md
├── 02_project-template.md
└── 03_ai-work-rules.md
```

## 00_index.md

Keep this as the routing table. It should answer: where should AI read the truth?

Include:

- User profile file.
- Project summary or handoff path.
- AI work rules.
- Conductor rules.
- Boss-view rules.

## 01_who-i-am.md

Capture:

- Identity and work context.
- Communication preferences.
- Tools the user uses.
- Hard prohibitions.
- A sample memory signal.

Do not store secrets, access tokens, personal IDs, or customer private data.

## 02_project-template.md

This is a blank master to copy, not a file to fill in place. One project = one file, at `~/vv-memory/projects/<short-name>.md`, copied from this master. Never write more than one project into this file itself, and never let a second project overwrite the first.

Each project should include:

- Problem being solved.
- Current state.
- Blocker type: decision, data, or execution.
- Three recommended next cards.
- Required user approvals.
- Out-of-scope boundaries.
- Truth sources.

## 03_ai-work-rules.md

Capture persistent behavior rules:

- Language and tone.
- Startup sequence.
- Red/yellow/green gates.
- Completion reporting format.
- Any project-specific exceptions.

## Onboarding Flow

Only use this after the user's first safe task or plan, and only when they want persistent memory. Ask or process seven answers, one at a time:

1. Who are you?
2. What tasks or projects do you want AI to help with?
3. What must AI never do on its own?
4. What should the coach call you, and do you want to rename vv?
5. How should AI talk to you?
6. What tools do you use?
7. What observable result would prove this AI system is useful?

Mark unknowns as `TBD`; never invent missing facts.
