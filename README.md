# vv 指揮家 v1.6.2

> 由 Vivi 老師打造

這是一套給「人 + AI」一起工作的公開包。

## 這是啥

如果你第一次看到這個 repo，可以先把它想成一包「AI 工作教練設定檔」。

下載這包之後，你不是得到一個普通聊天提示詞，而是得到一套管理 AI 的規則、記憶模板、開機流程和角色分工。它的目標是讓 Codex 或 Claude 不只是回答問題，而是能陪你把事情排好、拆開、驗收，並且知道哪些事不能亂做。

你可以叫它 `vv`。以後你在 Codex 裡打 `vv`，它就會啟動一整套管理 AI 的規則：先看你是誰、現在有哪些事在跑，再判斷這件事可以自動做，還是要先停下問你。

它有全域記憶。你可以把自己的背景、專案狀態、工作禁區寫進 `memory-templates/`，讓 AI 記得你是誰、專案做到哪、哪些事不能亂碰。

它也有開機規則。以後你打開新對話，只要打 `hi`，vv 就會先抓最新事件和進度接著聊，不用每次重新交代「我是誰、上次做到哪、這個案子卡在哪」。

裡面還有一組開發角色 agent，可以把一個專案拆成不同角色來協助你：PM 幫你釐清需求，架構師幫你想資料流和系統設計，UX 幫你看使用者體感，開發幫你落地，測試幫你找問題，發布幫你做上線前檢查。你不用一開始就講得很完整，vv 會幫你把模糊想法一步一步理順成能動工的計畫。

v1.6.2 的重點不是讓 AI 變成萬能助理，而是讓 AI 先知道三件事：

1. 你是誰。
2. 你現在有哪些事在跑。
3. 哪些事可以自動做，哪些事一定要先停下問你。

如果你是第一次打開，請照這個順序讀：

1. `README.md`：你現在看的這份，先搞懂整包怎麼用。
2. `指揮家.md`：AI 的主規則，負責判斷任務、派工、授權、驗收。
3. `vv-老闆視角.md`：每天或每次開工時，讓 AI 先用老闆視角幫你排序。
4. `onboarding.md`：第一次使用時，回答 6 題，建立你的 memory。
5. `memory-templates/`：把你的背景、專案、工作規則寫成 AI 看得懂的檔案。

## v1.6 跟 v1.5 差在哪

| v1.5 | v1.6 |
|---|---|
| 重點在「執行規則」：任務分級、派工、紅黃綠授權、驗收、停損 | 加上「記憶入口」：先讓 AI 認識你，再開始安全做事 |
| AI 開工時主要讀 `指揮家.md` | AI 開工時先讀 memory 訊號，再讀 `指揮家.md` |
| 比較適合已經有固定工作流的人 | 更適合第一次導入 AI 工作中樞的人 |
| 進度靠 `HANDOFF-LATEST.md` 接棒 | 進度仍靠 handoff，但新增「老闆視角」幫你提醒被遺忘的案 |

一句話：

v1.5 是「AI 做事前的安全規則」。
v1.6 是「AI 先認識你，再照安全規則做事」。

## 這包適合誰

- 創業者、主管、顧問、自由工作者。
- 手上很多案子，常常忘記哪個做到哪。
- 想用 Claude、Codex 或其他 AI 幫忙拆任務、寫文件、寫 code、驗收成果。
- 不想每次都重新解釋自己的背景、規則、禁區。

## Codex 正式 Skill 安裝方式

如果你要讓 Codex 真正自動辨識、可觸發、可長期維護，請安裝 `vv-conductor` skill：

```bash
mkdir -p ~/.codex/skills
cp -R ~/Desktop/vv-指揮家-v1.6/skills/vv-conductor ~/.codex/skills/
```

重開 Codex 後，當你說 `vv`、`指揮家`、`今天先做什麼`、`派工`、`紅黃綠`、`handoff`，Codex 就能觸發這個 skill。

## 更新 vv

如果新版出來，記得重新複製 `skills/vv-conductor` 覆蓋本機安裝版。

```bash
cp -R ~/Desktop/vv-指揮家-v1.6/skills/vv-conductor ~/.codex/skills/
```

Codex 實際讀的是 `~/.codex/skills/vv-conductor/` 裡的檔案。只更新 GitHub 或桌面資料夾，沒有覆蓋本機 skill 的話，新對話還是會一直跑舊版。

## 手動使用方式

把這個資料夾放在桌面後，先把 `指揮家.md` 複製到你的 home 目錄：

```bash
cp ~/Desktop/vv-指揮家-v1.6/指揮家.md ~/指揮家.md
```

再把 `memory-templates/` 複製到你固定放 AI 記憶的地方。你可以先放桌面，不急著工程化。

```bash
mkdir -p ~/vv-memory
cp ~/Desktop/vv-指揮家-v1.6/memory-templates/*.md ~/vv-memory/
```

之後在 AI 對話框開頭貼：

```text
請先讀 ~/指揮家.md，再讀 ~/vv-memory/00_索引.md，進入 vv 指揮家模式。
```

## 第一次要做什麼

打開 `onboarding.md`，回答 6 題。

回答完後，把答案整理進：

- `memory-templates/01_我是誰.md`
- `memory-templates/02_專案範本.md`
- `memory-templates/03_給AI的工作規則.md`

不需要一次寫很完美。v1.6 的設計是先有一版，工作一週後再養。

## 你可以怎麼叫 vv

```text
vv 我今天該先做什麼？
vv 幫我把這個需求拆成能施工的卡片。
vv 先讀我的 memory，再判斷這件事該不該做。
vv 幫我看這個專案現在卡在哪。
vv 這件事能不能自動跑？還是要我拍板？
```

## 檔案結構

```text
vv-指揮家-v1.6/
├── README.md
├── skill-index.md
├── 指揮家.md
├── vv-老闆視角.md
├── onboarding.md
├── agents/
├── memory-templates/
    ├── 00_索引.md
    ├── 01_我是誰.md
    ├── 02_專案範本.md
    └── 03_給AI的工作規則.md
└── skills/
    └── vv-conductor/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## 找 Vivi

台灣的朋友，加入 Vivi 的 LINE 官方帳號，
卡關可以直接問、也會收到 vv 更新通知：
https://lin.ee/ZgPigfa

## 這包現在分三層

### 1. 人看的公開文件

- `README.md`
- `指揮家.md`
- `vv-老闆視角.md`
- `onboarding.md`

### 2. 記憶模板

- `memory-templates/00_索引.md`
- `memory-templates/01_我是誰.md`
- `memory-templates/02_專案範本.md`
- `memory-templates/03_給AI的工作規則.md`

### 3. 正式 skill

- `skill-index.md`
- `skills/vv-conductor/SKILL.md`
- `skills/vv-conductor/agents/openai.yaml`
- `skills/vv-conductor/references/*.md`
