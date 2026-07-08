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

Ask or process six answers:

1. Who are you?
2. What are your top three projects?
3. What must AI never do on its own?
4. How should AI talk to you?
5. What tools do you use?
6. What observable result would prove this AI system is useful?

Mark unknowns as `待補`; never invent missing facts.

