#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
skill_file="$repo_dir/skills/vv-conductor/SKILL.md"
start_file="$repo_dir/skills/vv-conductor/references/beginner-safety-start.md"

grep -Fq 'Greeting only:' "$skill_file"
grep -Fq 'Task already stated:' "$skill_file"
grep -Fq 'Do not repeat the first-task question' "$skill_file"
grep -Fq 'If the user already stated a task, do not ask this question again.' "$start_file"

printf 'PASS: greeting asks one first-task question; stated task is acknowledged without repetition\n'
