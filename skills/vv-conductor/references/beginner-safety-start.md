# Beginner Safety Start

Use this flow when the user is new, their Vault is missing or still blank, or they ask for the "kickoff playbook".

The goal is to help the user carry out the small task selected in question 6 safely.

## First Question

After the required introduction and contact block, ask only:

```text
What do you most want Codex or Claude Code to help you with right now? One sentence is enough.
```

If installation onboarding is active, this task comes from question 6. Do not ask for it again.

## Before Doing the Task

Reply in plain language and cover these points in a compact form:

1. **What I understand you need**: repeat the task in one sentence.
2. **Possible risks**: name only risks that actually apply.
3. **A safe first version**: shrink the task to the smallest useful result.
4. **What I won't touch this time**: state the boundary clearly.
5. **What's still missing**: ask only for information that blocks safe progress.
6. **How we'll know it's done**: give a result the user can check.
7. **Which actions need your go-ahead first**: call out any action that needs explicit approval.

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
Your first task is safely underway. I've also saved the first version of your background and no-go zones, so next time you can start with `vv + what you want to do`.
```

Keep helping with the selected task after this bridge.
