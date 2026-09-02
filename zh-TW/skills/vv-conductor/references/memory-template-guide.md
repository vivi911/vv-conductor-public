# Memory Template Guide

Use this reference when vv-pack-1.7.2 saves the six first-install answers into the user's memory.

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

This is a blank master to copy, not a file to fill in place. One project = one file, at `~/vv-memory/專案/<short-name>.md`, copied from this master. Never write more than one project into this file itself, and never let a second project overwrite the first.

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

第一次安裝時，先一題一題問完以下六題，再開始使用者選定的小任務：

1. 先簡單介紹自己，平常在忙什麼？
2. 陪跑教練該怎麼稱呼你？
3. AI 熟悉度 0 到 10 分是幾分？最近用 AI 做過什麼？
4. 平常用哪些 AI 或工作工具？
5. 有哪些事不希望 AI 自己亂做？
6. 現在最想完成的第一件小事是什麼？

Mark unknowns as `待補`; never invent missing facts.
