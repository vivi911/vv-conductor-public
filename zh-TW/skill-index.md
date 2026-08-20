# skill-index

這份檔案是「AI 陪跑教練」公開包的 skill 入口索引。技術名稱保留 `vv-conductor`，讓既有安裝與觸發方式繼續可用。

## 目前正式 skill

| Skill | 路徑 | 用途 |
|---|---|---|
| vv-conductor | `zh-TW/skills/vv-conductor/SKILL.md` | 讓 Codex／Claude Code 先陪新手安全完成第一個任務，再接上記憶、派工、紅黃綠授權、驗收與 handoff |

## 什麼時候會觸發

使用者說到以下任一類型時，應使用 `vv-conductor`：

- `vv`
- `vivi`
- `AI 陪跑教練`
- `陪跑教練`
- `開工手冊`
- `指揮家`
- `conductor`
- `派工`
- `今天先做什麼`
- `我有點亂`
- `幫我排優先序`
- `紅黃綠`
- `handoff`
- `memory templates`
- `用 vv v1.6 工作流`

## 安裝方式

Codex 和 Claude Code 都可安裝同一份 `zh-TW/skills/vv-conductor/` 資料夾。差別只有目標目錄。

Codex：

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/vv-conductor
cp -R ~/vv-conductor-public/zh-TW/skills/vv-conductor ~/.codex/skills/vv-conductor
```

Claude Code：

```bash
mkdir -p ~/.claude/skills
rm -rf ~/.claude/skills/vv-conductor
cp -R ~/vv-conductor-public/zh-TW/skills/vv-conductor ~/.claude/skills/vv-conductor
```

重開之後，`vv-conductor` 會成為可觸發 skill。兩邊都裝也不會互相影響。

**English version**：這包也有預設的英文版，放在根目錄 [`../README.md`](../README.md)（`skills/vv-conductor/`）。兩個語言包裝到同一個目標資料夾名稱（`~/.claude/skills/vv-conductor/` 或 `~/.codex/skills/vv-conductor/`），只能選一種語言裝——都裝的話後裝的會蓋掉先裝的。

如果你用的 AI 工具沒有 skill 目錄機制，退而求其次：把 `SKILL.md` 和 `references/` 底下的檔案放進該工具的規則或專案知識裡，並在對話開頭請它先讀。

## 維護規則

- `SKILL.md` 保持短，只放觸發、流程、必要判斷。
- 詳細規則放 `references/`。
- 改完 `SKILL.md` 要跑 validator。
- 對外分享前要掃敏感資訊。
