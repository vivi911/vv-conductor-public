# Package Maintenance

Use this reference when updating, packaging, validating, or installing the `AI 陪跑教練` public package (`vv-conductor`, Traditional Chinese track).

## Public Package Layout

English is the default track, at the repo root. This Traditional Chinese track lives one level down, under `zh-TW/`, mirroring the same structure.

```text
vv-conductor-public/
├── README.md          (English, default)
├── skills/vv-conductor/  (English, default)
└── zh-TW/
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

Keep the two trees structurally identical — same relative paths, same file roles — so a fix to one track's structure has an obvious counterpart in the other.

## Install Target

Codex and Claude Code can both install the same `vv-conductor` folder. Only the target directory differs. Point the `cp` source at `zh-TW/skills/vv-conductor` for this Chinese pack (or `skills/vv-conductor` for the English pack — pick one language, not both, since they install to the same target path).

⚠️ Remove the destination first. On macOS, `cp -R src dst` where `dst` already exists copies *into* it, producing `vv-conductor/vv-conductor` — so re-running the install (which is exactly what updating does) silently nests instead of replacing, and the user keeps running the old version with no error.

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/vv-conductor
cp -R <本包路徑>/zh-TW/skills/vv-conductor ~/.codex/skills/vv-conductor
```

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/vv-conductor
cp -R <本包路徑>/zh-TW/skills/vv-conductor ~/.claude/skills/vv-conductor
```

For any other agent without a skill directory, copy the package docs into its configured rule or project-knowledge area according to that tool's conventions.

## Validation

Run the official validator after editing `SKILL.md`:

```bash
python3 <你的 skill-creator 安裝路徑>/scripts/quick_validate.py <本包路徑>/zh-TW/skills/vv-conductor
```

## Consistency Gate (required before every publish)

The same rule often lives in several files, and in two language tracks: `SKILL.md` (what the AI executes), `conductor.md` / `指揮家.md` (human-readable mirror), `onboarding.md` (first-run flow), and `references/` (supplementary detail). Edit one and forget another — or edit one language track and forget the other — and the rules silently contradict each other. There is no error message; the AI just picks a different behaviour depending on which file, or which language track, it read.

Run this after **every** edit to any rule file, before committing or publishing:

```bash
python3 <本包路徑>/scripts/check-consistency.py
```

It scans every rule file in both language tracks for cross-file mismatches, checks that required content was not accidentally dropped, and verifies every file reference still resolves. Do not publish on red.

The script's own self-test runs first and must pass before it trusts its own results — if the self-test fails, the checkers themselves may be broken, and a green result would be a false green. Treat a self-test failure the same as a red result: stop and fix it before publishing.

Package with macOS-friendly zip:

```bash
ditto -c -k --keepParent vv-conductor-zh-TW-v1.7 vv-conductor-zh-TW-v1.7.zip
```

Verify by extracting to `/private/tmp` and counting key files.

## Privacy Scan

Before sharing publicly, scan for:

```text
UID, access token, API key, secret command, project id, customer name, private project name, personal phone/email, payment data
```

Concept words like `token`, `secret`, or `rotate key` are acceptable when describing safety rules, but actual values or command strings are not.
