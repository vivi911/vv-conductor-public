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

## Codex 安裝方式

把 skill 資料夾複製到 Codex skills 目錄：

```bash
mkdir -p ~/.codex/skills
cp -R ~/Desktop/vv-指揮家-v1.6/skills/vv-conductor ~/.codex/skills/
```

重開 Codex 後，`vv-conductor` 會成為可觸發 skill。

## Claude 使用方式

Claude 若沒有同一套 skill 安裝機制，就把以下檔案放到 Claude 會讀的規則或專案知識中：

- `skills/vv-conductor/SKILL.md`
- `skills/vv-conductor/references/vv-conductor-reference.md`
- `skills/vv-conductor/references/memory-template-guide.md`
- `skills/vv-conductor/references/package-maintenance.md`

## 維護規則

- `SKILL.md` 保持短，只放觸發、流程、必要判斷。
- 詳細規則放 `references/`。
- 改完 `SKILL.md` 要跑 validator。
- 對外分享前要掃敏感資訊。

