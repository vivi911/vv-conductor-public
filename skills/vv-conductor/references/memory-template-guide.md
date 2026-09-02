# Memory Template Guide

Use this reference when vv-pack-1.7.2 saves the six first-install answers into the user's memory.

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

On first installation, ask or process these six answers one at a time before starting the selected small task:

1. Who are you and what are you usually busy with?
2. What should the coach call you?
3. How familiar are you with AI, from 0 to 10, and what have you used it for?
4. Which AI tools do you normally use?
5. What must AI never do on its own?
6. What is the first small task you want to complete?

Mark unknowns as `TBD`; never invent missing facts.
