# Package Maintenance

Use this reference when updating, packaging, validating, or installing the `AI 陪跑教練` public package (`vv-conductor`).

## Public Package Layout

```text
vv-conductor-public/
├── README.md
├── VERSION
├── skill-index.md
├── 指揮家.md
├── vv-老闆視角.md
└── skills/
    └── vv-conductor/
        ├── SKILL.md
        ├── VERSION
        ├── onboarding.md
        ├── agents/openai.yaml
        ├── memory-templates/
        └── references/
            ├── beginner-safety-start.md
            ├── memory-template-guide.md
            ├── package-maintenance.md
            └── vv-conductor-reference.md
```

## Install Target

Codex and Claude Code can both install the same `vv-conductor` folder. Only the target directory differs.

```bash
mkdir -p ~/.codex/skills
cp -R <本包路徑>/skills/vv-conductor ~/.codex/skills/
```

```bash
mkdir -p ~/.claude/skills
cp -R <本包路徑>/skills/vv-conductor ~/.claude/skills/
```

Both may be installed side by side. For any other agent without a skill directory, copy the package docs into its configured rule or project-knowledge area according to that tool's conventions.

## Validation

Run the official validator after editing `SKILL.md`:

```bash
python3 <你的 skill-creator 安裝路徑>/scripts/quick_validate.py <本包路徑>/skills/vv-conductor
```

## Consistency Gate (required before every publish)

The same rule often lives in several files: `SKILL.md` (what the AI executes), `指揮家.md` (human-readable mirror), `onboarding.md` (first-run flow), and `references/` (supplementary detail). Edit one and forget another, and the rules silently contradict each other — there is no error message, the AI just picks a different behaviour depending on which file it read.

Run this after **every** edit to any rule file, before committing or publishing:

```bash
python3 <本包路徑>/scripts/check-consistency.py
```

It scans every rule file for cross-file mismatches, checks that required content was not accidentally dropped, and verifies every file reference still resolves. Do not publish on red.

The script's own self-test runs first and must pass before it trusts its own results — if the self-test fails, the checkers themselves may be broken, and a green result would be a false green. Treat a self-test failure the same as a red result: stop and fix it before publishing.

Package with macOS-friendly zip:

```bash
ditto -c -k --keepParent vv-指揮家-v1.6 vv-指揮家-v1.6.zip
```

Verify by extracting to `/private/tmp` and counting key files.

## Privacy Scan

Before sharing publicly, scan for:

```text
UID, access token, API key, secret command, project id, customer name, private project name, personal phone/email, payment data
```

Concept words like `token`, `secret`, or `rotate key` are acceptable when describing safety rules, but actual values or command strings are not.
