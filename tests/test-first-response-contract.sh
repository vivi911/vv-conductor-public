#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
skill_file="$repo_dir/skills/vv-conductor/SKILL.md"
onboarding_file="$repo_dir/onboarding.md"

grep -Fq 'Greeting only:' "$skill_file"
grep -Fq 'Task already stated:' "$skill_file"
grep -Fq 'Do not repeat the first-task question' "$skill_file"
grep -Fq 'follow `onboarding.md` and ask question 1' "$skill_file"
grep -Fq '### 1. 先簡單介紹一下你自己，好嗎？' "$onboarding_file"
grep -Fq '### 7. 我們先從你最想完成的一件小事開始' "$onboarding_file"
grep -Fq '不是可靠的系統啟動暗號' "$onboarding_file"

printf 'PASS: greeting starts guided onboarding; stated task is acknowledged without repetition\n'
