# Package Maintenance

Use this reference when updating, packaging, validating, or installing `vv-指揮家-v1.6`.

## Public Package Layout

```text
vv-conductor-public/
├── README.md
├── VERSION
├── skill-index.md
├── 指揮家.md
├── vv-老闆視角.md
├── onboarding.md
├── memory-templates/
└── skills/
    └── vv-conductor/
        ├── SKILL.md
        ├── VERSION
        ├── agents/openai.yaml
        └── references/
```

## Install Target

Codex and Claude share the same skill-discovery mechanism; the `vv-conductor` folder is copied verbatim and its contents need no per-tool changes. Only the target directory differs.

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

