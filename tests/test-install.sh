#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
temporary_root="$(mktemp -d)"
trap 'rm -rf "$temporary_root"' EXIT

fake_home="$temporary_root/home"
fake_bin="$temporary_root/bin"
mkdir -p "$fake_home/.codex" "$fake_home/.claude" "$fake_bin"
touch "$fake_bin/codex" "$fake_bin/claude"
chmod +x "$fake_bin/codex" "$fake_bin/claude"

output="$(VV_HOME="$fake_home" PATH="$fake_bin:$PATH" bash "$repo_dir/install.sh")"
test -f "$fake_home/.codex/skills/vv-conductor/SKILL.md"
test -f "$fake_home/.claude/skills/vv-conductor/SKILL.md"
printf '%s' "$output" | grep -Fq '不用選平台'
printf '%s' "$output" | grep -Fq '不用背 hi、vv'

printf 'old installation' > "$fake_home/.codex/skills/vv-conductor/legacy.txt"
VV_HOME="$fake_home" PATH="$fake_bin:$PATH" bash "$repo_dir/install.sh" >/dev/null
test ! -e "$fake_home/.codex/skills/vv-conductor/legacy.txt"
find "$fake_home/.codex/skills" -maxdepth 1 -type d -name 'vv-conductor.vv-backup-*' -exec test -f '{}/legacy.txt' \;

empty_home="$temporary_root/empty-home"
mkdir -p "$empty_home"
set +e
VV_HOME="$empty_home" PATH="/usr/bin:/bin" bash "$repo_dir/install.sh" >/dev/null 2>&1
status=$?
set -e
test "$status" -eq 2

printf 'PASS: automatic multi-platform install and unsupported-machine guard\n'
