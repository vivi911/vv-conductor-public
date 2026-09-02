#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
skill_file="$repo_dir/skills/vv-conductor/SKILL.md"
onboarding_file="$repo_dir/onboarding.md"
installed_onboarding_file="$repo_dir/skills/vv-conductor/onboarding.md"
readme_file="$repo_dir/README.md"

grep -Fq 'Greeting only:' "$skill_file"
grep -Fq 'Task already stated:' "$skill_file"
grep -Fq 'Do not repeat the first-task question' "$skill_file"
grep -Fq 'follow `onboarding.md` and ask question 1' "$skill_file"
grep -Fq '### 1. 先簡單介紹一下你自己，好嗎？' "$onboarding_file"
grep -Fq '### 6. 我們先從你最想完成的一件小事開始' "$onboarding_file"
if grep -Fq '你想怎麼叫我' "$onboarding_file"; then
  printf 'FAIL: onboarding still asks the user to rename vv\n' >&2
  exit 1
fi
cmp -s "$onboarding_file" "$installed_onboarding_file"
grep -Fq '安裝與檢查完成後，不要停在安裝報告，也不要等我再打 `hi` 或 `vv`' "$readme_file"
grep -Fq '直接讀取已安裝的 `onboarding.md`，在同一個對話問第 1 題' "$readme_file"
grep -Fq '<a id="the-fastest-way-let-your-ai-install-it"></a>' "$readme_file"
grep -Fq '第一次安裝不用打啟動詞；以後重新開對話時' "$readme_file"
grep -Fq 'vv，我想做 XXX。' "$readme_file"
grep -Fq 'vv，請幫我做 XXX。' "$readme_file"
grep -Fq 'vv，還有哪些沒完成？' "$readme_file"
if grep -Fq '這時它才會打開 `onboarding.md`' "$readme_file"; then
  printf 'FAIL: README still postpones onboarding until after the first task\n' >&2
  exit 1
fi

printf 'PASS: installer continues directly to question 1; greeting and stated-task branches remain explicit\n'
