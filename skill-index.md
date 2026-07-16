# skill-index

這份檔案是 `vv-指揮家-v1.6` 的 skill 入口索引。

## 目前正式 skill

| Skill | 路徑 | 用途 |
|---|---|---|
| vv-conductor | `skills/vv-conductor/SKILL.md` | 讓 Codex/Claude 以 vv 指揮家模式工作：先讀記憶、回記憶訊號、判斷老闆視角或執行模式、套紅黃綠授權、做驗收與 handoff |

## 什麼時候會觸發

使用者說到以下任一類型時，應使用 `vv-conductor`：

- `vv`
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

Codex 和 Claude 讀 skill 的機制相同，`skills/vv-conductor/` 資料夾原封不動複製過去即可，內容不需要改。差別只有目標目錄。

Codex：

```bash
mkdir -p ~/.codex/skills
cp -R ~/vv-conductor-public/skills/vv-conductor ~/.codex/skills/
```

Claude：

```bash
mkdir -p ~/.claude/skills
cp -R ~/vv-conductor-public/skills/vv-conductor ~/.claude/skills/
```

重開之後，`vv-conductor` 會成為可觸發 skill。兩邊都裝也不會互相影響。

如果你用的 AI 工具沒有 skill 目錄機制，退而求其次：把 `SKILL.md` 和 `references/` 底下的檔案放進該工具的規則或專案知識裡，並在對話開頭請它先讀。

## 維護規則

- `SKILL.md` 保持短，只放觸發、流程、必要判斷。
- 詳細規則放 `references/`。
- 改完 `SKILL.md` 要跑 validator。
- 對外分享前要掃敏感資訊。

