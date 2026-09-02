# Beginner Safety Start

Use this flow when the user is new, their Vault is missing or still blank, or they ask for `開工手冊`.

The goal is to help the user carry out the small task selected in question 6 safely.

## First Question

After the required introduction and contact block, ask only:

```text
你現在最想請 Codex 或 Claude Code 幫你做什麼？用一句話說就好。
```

If installation onboarding is active, this task comes from question 6. Do not ask for it again.

## Before Doing the Task

Reply in plain language and cover these points in a compact form:

1. **我理解的需求**：repeat the task in one sentence.
2. **可能的風險**：name only risks that actually apply.
3. **安全的第一版**：shrink the task to the smallest useful result.
4. **這次不會碰的東西**：state the boundary clearly.
5. **還缺什麼**：ask only for information that blocks safe progress.
6. **怎麼算完成**：give a result the user can check.
7. **哪些動作要先問**：call out any action that needs explicit approval.

Always pair a risk with a safe first step. Do not scare the user with a list of abstract dangers.

## Hard Safety Boundary

Without explicit user approval, do not:

- publish, deploy, send, buy, pay, or spend advertising budget;
- change a live account, production system, real customer data, or external platform;
- delete or overwrite material data;
- grant permissions, change OAuth access, rotate keys, or expose secrets;
- claim that a result is live or complete without checking it.

Read-only inspection, drafting, local files, reversible edits, and local verification are the preferred first moves.

## Bridge to the Full Coach

After onboarding question 6, use this flow to start the selected task. Do not offer another onboarding interview.

```text
第一個任務已經安全開工。我也存下了你的第一版背景和工作禁區；下次直接用「vv＋想做的事」開始。
```

Keep helping with the selected task after this bridge.
