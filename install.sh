#!/usr/bin/env bash
# Install vv for every supported AI workspace found on this computer.
set -euo pipefail

repo_url="https://github.com/vivi911/vv-conductor-public.git"
user_home="${VV_HOME:-$HOME}"
script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
package_dir="$script_dir"

if [[ ! -f "$package_dir/skills/vv-conductor/SKILL.md" ]]; then
  if ! command -v git >/dev/null 2>&1; then
    printf '無法安裝：這台電腦需要先有 Git，才能安全下載 vv 公開包。\n' >&2
    exit 3
  fi
  package_dir="$user_home/vv-conductor-public"
  if [[ -d "$package_dir/.git" ]]; then
    git -C "$package_dir" pull --ff-only
  elif [[ ! -e "$package_dir" ]]; then
    git clone "$repo_url" "$package_dir"
  else
    printf '無法安裝：%s 已存在，但不是 vv 的 Git 資料夾。\n' "$package_dir" >&2
    exit 1
  fi
fi

skill_source="$package_dir/skills/vv-conductor"
if [[ ! -f "$skill_source/SKILL.md" ]]; then
  printf '無法安裝：找不到 vv 的核心檔案。\n' >&2
  exit 1
fi

targets=()
if [[ -d "$user_home/.codex" ]] || command -v codex >/dev/null 2>&1; then
  targets+=("$user_home/.codex/skills")
fi
if [[ -d "$user_home/.claude" ]] || command -v claude >/dev/null 2>&1; then
  targets+=("$user_home/.claude/skills")
fi

if [[ ${#targets[@]} -eq 0 ]]; then
  printf '還沒找到 Codex 或 Claude Code，因此沒有安裝到錯的地方。先安裝其中一個，再重新執行這一行即可。\n' >&2
  exit 2
fi

installed=()
for target in "${targets[@]}"; do
  destination="$target/vv-conductor"
  mkdir -p "$target"
  if [[ -e "$destination" ]]; then
    backup="$destination.vv-backup-$(date +%Y%m%d%H%M%S)"
    mv "$destination" "$backup"
  fi
  cp -R "$skill_source" "$destination"
  installed+=("$destination")
done

printf 'vv 已安裝完成：\n'
for installed_path in "${installed[@]}"; do
  printf '• %s\n' "$installed_path"
done
printf '\n如果是 Codex 或 Claude Code 在這個對話幫你安裝，它應該現在直接讀 onboarding.md 並問第 1 題，不等你再輸入。\n'
printf '如果你是自己在終端機執行，請開一個新的 Codex 或 Claude Code 對話，直接用白話說你想做的事。\n'
printf '不用選平台、不用背 hi、vv 或其他觸發詞。\n'
