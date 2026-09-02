# Memory Template Guide

Use this reference when the user wants vv v1.6 to remember who they are, what projects are running, or what AI should never do.

## Required Files

```text
memory-templates/
├── 00_索引.md
├── 01_我是誰.md
├── 02_專案範本.md
└── 03_給AI的工作規則.md
```

## 00_索引.md

Keep this as the routing table. It should answer: where should AI read the truth?

Include:

- User profile file.
- Project summary or handoff path.
- AI work rules.
- Conductor rules.
- Boss-view rules.

## 01_我是誰.md

Capture:

- Identity and work context.
- Communication preferences.
- Tools the user uses.
- Hard prohibitions.
- A sample memory signal.

Do not store secrets, access tokens, personal IDs, or customer private data.

## 02_專案範本.md

Each project should include:

- Problem being solved.
- Current state.
- Blocker type: decision, data, or execution.
- Three recommended next cards.
- Required user approvals.
- Out-of-scope boundaries.
- Truth sources.

## 03_給AI的工作規則.md

Capture persistent behavior rules:

- Language and tone.
- Startup sequence.
- Red/yellow/green gates.
- Completion reporting format.
- Any project-specific exceptions.

## Onboarding Flow

For an AI-driven first install, ask or process these six answers one at a time. Outside the install path, do not interrupt a stated task to force onboarding:

1. Who are you and what do you usually work on?
2. What should the coach call you?
3. How familiar are you with AI from 0 to 10, and what is one recent example?
4. What AI or work tools do you use?
5. What must AI never do on its own?
6. What first small task do you want to complete?

Mark unknowns as `待補`; never invent missing facts.
