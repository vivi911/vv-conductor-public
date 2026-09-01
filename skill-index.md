# skill-index

這份檔案是「AI 陪跑教練」公開包的 skill 入口索引。技術名稱保留 `vv-conductor`，讓既有安裝與觸發方式繼續可用。

## 目前正式 skill

| Skill | 路徑 | 用途 |
|---|---|---|
| vv-conductor | `skills/vv-conductor/SKILL.md` | 讓 Codex／Claude Code 先陪新手安全完成第一個任務，再接上記憶、派工、紅黃綠授權、驗收與 handoff |

## 什麼時候會觸發

使用者說到以下任一類型時，應使用 `vv-conductor`：

- `vv`
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

只要貼一行。它會自動偵測已安裝的 Codex 與 Claude Code，並安裝到所有找到的工具；不要求使用者先回答平台名稱。

```bash
curl -fsSL https://raw.githubusercontent.com/vivi911/vv-conductor-public/main/install.sh | bash
```

重開工具後，使用者直接用白話講第一件事，不需要背觸發詞。聊天工具不能在使用者送出第一句話前自行說話，這是平台限制，不是使用者漏做了設定。

如果你用的 AI 工具沒有 skill 目錄機制，退而求其次：把 `SKILL.md` 和 `references/` 底下的檔案放進該工具的規則或專案知識裡，並在對話開頭請它先讀。

## 維護規則

- `SKILL.md` 保持短，只放觸發、流程、必要判斷。
- 詳細規則放 `references/`。
- 改完 `SKILL.md` 要跑 validator。
- 對外分享前要掃敏感資訊。
