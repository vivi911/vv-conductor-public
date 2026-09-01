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
├── onboarding.md
├── memory-templates/
└── skills/
    └── vv-conductor/
        ├── SKILL.md
        ├── VERSION
        ├── agents/openai.yaml
        └── references/
            ├── beginner-safety-start.md
            ├── memory-template-guide.md
            ├── package-maintenance.md
            └── vv-conductor-reference.md
```

## Install Target

Use `install.sh` as the only normal install route. It detects Codex and Claude Code from their local folders or commands, then installs to every detected target without asking the beginner to choose.

```bash
bash <本包路徑>/install.sh
```

If an older vv installation already exists, the installer moves that exact skill folder aside as a timestamped backup before copying the new one. For any other agent without a skill directory, copy the package docs into its configured rule or project-knowledge area according to that tool's conventions.

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
