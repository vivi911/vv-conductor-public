#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

check_tree() {
  skill_file=$1
  onboarding_file=$2

  question_count=$(grep -Ec '^### [1-6]\.' "$onboarding_file")
  [ "$question_count" -eq 6 ]
  ! grep -Eiq 'rename vv|want to give (me|the coach) a name|想幫(我|教練)取(個)?名字|替 vv 改名|你想怎麼叫這位陪跑教練' "$skill_file" "$onboarding_file"
  ! grep -Eiq '7[- ]question|7 questions|7 Vault questions|7 題|7 個問題|七題|第 7 題' "$skill_file" "$onboarding_file"
  grep -Fq 'question 1' "$skill_file" || grep -Fq '第 1 題' "$skill_file"
  grep -Fq 'question 6' "$skill_file" || grep -Fq '第 6 題' "$skill_file"
}

check_tree "$root_dir/skills/vv-conductor/SKILL.md" "$root_dir/skills/vv-conductor/onboarding.md"
check_tree "$root_dir/zh-TW/skills/vv-conductor/SKILL.md" "$root_dir/zh-TW/skills/vv-conductor/onboarding.md"

grep -Fq 'Do not wait for me to type hi, vv, or another trigger.' "$root_dir/README.md"
grep -Fq '不要等我打 hi、vv 或任何啟動詞。' "$root_dir/zh-TW/README.md"
grep -Fq 'vv + task' "$root_dir/README.md"
grep -Fq 'vv＋任務' "$root_dir/zh-TW/README.md"

echo 'PASS: bilingual first-run contract uses six questions, no coach rename, same-chat start, and vv + task later.'
