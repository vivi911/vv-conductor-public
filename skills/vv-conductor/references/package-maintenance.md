# Package Maintenance

Use this reference when updating, packaging, validating, or installing `vv-指揮家-v1.6`.

## Public Package Layout

```text
vv-指揮家-v1.6/
├── README.md
├── skill-index.md
├── 指揮家.md
├── vv-老闆視角.md
├── onboarding.md
├── memory-templates/
└── skills/
    └── vv-conductor/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## Install Target

For Codex auto-discovery, copy the skill folder:

```bash
mkdir -p ~/.codex/skills
cp -R <本包路徑>/skills/vv-conductor ~/.codex/skills/
```

For Claude or another agent, copy the package docs into its configured skill or rule directory according to that tool's conventions.

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

