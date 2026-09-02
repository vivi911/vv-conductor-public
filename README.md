# AI 陪跑教練（vv）v1.7.2 候選版

> 安裝完直接問 7 個短問題；認識你後，立刻陪你完成第一件小事。

這是一套給「人 + AI」一起工作的公開包。

## Vivi 老師是誰

Vivi 老師是 GoAskVivi 的創作者，長期用 Codex、Claude Code 和各種 AI 工具一起做真實專案：寫文件、拆任務、做網站、改流程、整理知識、驗收成果。

## 為什麼有 AI 陪跑教練

過去 7 個月，Vivi 老師幾乎每天花 10 小時以上跟 AI 一起工作——寫文件、拆任務、做網站、改流程、上線驗收。中間踩過大量的坑：AI 亂改檔案、忘記你是誰、自己上線出事、把小事做成大工程、嘴上說「完成了」其實根本沒驗證。

AI 陪跑教練就是把這 7 個月、每天 10 小時以上的踩坑經驗，蒸餾成一套規則。原本獨立的「開工手冊」已整合成第一次使用的安全開工流程，背後仍由 vv 指揮家負責記憶、派工與驗收。

它的目標很單純：讓一個剛開始用 AI 的小白，也能像旁邊坐了一個開車教練。你握方向盤（做決定），AI 負責開（做事），vv 幫你看路、提醒、必要時踩剎車——指揮 AI 往你要的方向走，不會讓它亂跑、亂闖、亂出事。

## 怎麼認識 Vivi 老師

想認識 Vivi 老師和 GoAskVivi 的 AI 工作方法，先看官網——GoAskVivi 是 Vivi 老師分享 AI 實戰、Vibe Coding 心法與線上課程的地方：
https://goaskvivi.com/

台灣的朋友，加 Vivi 的 LINE 官方帳號。卡關可以直接問，也會收到 vv 更新通知：
https://lin.ee/ZgPigfa

香港・大陸的朋友，打開小紅書 App 搜尋小紅書號「940160605」（帳號：Vivi｜品牌操盤 22 年｜AI 实战派），追蹤後私訊即可。

## 這是啥

如果你第一次看到這個 repo，可以先把它想成一包「AI 工作教練設定檔」。

它不是一個需要你看懂程式碼的工具，而是一組 `.md` 檔案。`.md` 就是 Markdown 文件，白話說，就是 AI 看得懂、你也看得懂的工作說明書。

這套 AI 陪跑教練不是單純教你「怎麼問 AI」。請 Codex 或 Claude Code 安裝完後，它會在同一個對話直接用 7 個短問題認識你，再帶你完成第一件小事。之後開新對話時，直接說出任務就好。

下載這包之後，你不是得到一個普通聊天提示詞，而是一套給 Codex 或 Claude Code 使用的安全開工、記憶、派工和驗收規則。

安裝後不用記得叫它什麼。平常開一個新對話框，直接用白話說你想做的事，它就會先幫你安全開工：先理解需求、縮小第一版，再判斷哪些事可以自動做、哪些事要先停下問你。

它有全域記憶，這個記憶庫就叫 **Vault**。你可以把自己的背景、專案狀態、工作禁區寫進 `memory-templates/`（也就是你的 Vault），讓 AI 記得你是誰、專案做到哪、之前跟你協作過什麼、哪些事不能亂碰。

一般 AI 像失憶症，每次開新對話都要你重講一遍自己是誰；Vault 就是讓 AI「記得你」的那個地方。第一次只打招呼時，vv 會用幾個短問題幫你建立第一版，不是考試；建立後，它會先讀 Vault，再接著上次的進度繼續。

它也有開機規則。以後你打開新對話，直接說事情就好；vv 會先抓最新事件和進度接著聊，不用每次重新交代「我是誰、上次做到哪、這個案子卡在哪」。

裡面還有一組開發角色 agent，可以把一個專案拆成不同角色來協助你：PM 幫你釐清需求，架構師幫你想資料流和系統設計，UX 幫你看使用者體感，開發幫你落地，測試幫你找問題，發布幫你做上線前檢查。你不用一開始就講得很完整，vv 會幫你把模糊想法一步一步理順成能動工的計畫。

這一版的重點不是讓 AI 變成萬能助理，而是讓 AI 先知道三件事：

1. 你是誰。
2. 你現在有哪些事在跑。
3. 哪些事可以自動做，哪些事一定要先停下問你。

如果你是第一次打開，請照這個順序讀：

1. `README.md`：你現在看的這份，先搞懂整包怎麼用。
2. `指揮家.md`：AI 的主規則，負責判斷任務、派工、授權、驗收。
3. `vv-老闆視角.md`：每天或每次開工時，讓 AI 先用老闆視角幫你排序。
4. `skills/vv-conductor/references/beginner-safety-start.md`：第一次使用時的安全開工流程。
5. `memory-templates/`：把你的背景、專案、工作規則寫成 AI 看得懂的檔案。
6. `onboarding.md`：安裝完後，vv 在同一個對話用 7 題短問答建立第一版記憶。

## 平常對話怎麼開始

第一次安裝不用打啟動詞；以後重新開對話時，可以用 `vv` 開頭，再直接講你要做的事。

例如：

```text
vv，我想做 XXX。
vv，請幫我做 XXX。
vv，還有哪些沒完成？
```

不用照抄 `XXX`，換成你自己的事就好。一句話：**第一次安裝後會自動開始；以後重開對話，先叫 `vv`，再說你要做的事**。

## v1.6 跟 v1.5 差在哪

| v1.5 | v1.6 |
|---|---|
| 重點在「執行規則」：任務分級、派工、紅黃綠授權、驗收、停損 | 加上「記憶入口」：先讓 AI 認識你，再開始安全做事 |
| AI 開工時主要讀 `指揮家.md` | AI 開工時先讀 memory 訊號，再讀 `指揮家.md` |
| 比較適合已經有固定工作流的人 | 更適合第一次導入 AI 工作中樞的人 |
| 進度靠 `HANDOFF-LATEST.md` 接棒 | 進度仍靠 handoff，但新增「老闆視角」幫你提醒被遺忘的案 |

一句話：

v1.5 是「AI 做事前的安全規則」。
v1.7.2 是「安裝只送出一次；安裝完在同一個對話直接問第 1 題，不用再打 `hi` 或 `vv`」。

## 這包適合誰

- 創業者、主管、顧問、自由工作者。
- 手上很多案子，常常忘記哪個做到哪。
- 想用 Claude Code、Codex 或其他 AI 幫忙拆任務、寫文件、寫 code、驗收成果。
- 不想每次都重新解釋自己的背景、規則、禁區。

<a id="the-fastest-way-let-your-ai-install-it"></a>

## 最推薦：讓 Codex 或 Claude Code 幫你安裝

把下面整段貼進你現在開著的 Codex 或 Claude Code，只要送出這一次：

```text
請幫我安裝 AI 陪跑教練（vv）。請執行公開包的 install.sh，讓它自動找到這台電腦上的 Codex 或 Claude Code；安裝前先說明會動到哪些資料夾，舊版一律先留可回復備份，不要刪除我的記憶。

安裝與檢查完成後，不要停在安裝報告，也不要等我再打 `hi` 或 `vv`。請直接讀取已安裝的 `onboarding.md`，在同一個對話問第 1 題；一次只問一題。
```

因為是目前對話裡的 AI 幫你安裝，它能在安裝完的同一次回覆，立刻開始第 1 題。你不需要再輸入任何啟動詞。

## 備用：自己在終端機安裝

打開「終端機」（Terminal），整段貼上後按 Enter：

```bash
curl -fsSL https://raw.githubusercontent.com/vivi911/vv-conductor-public/main/install.sh | bash
```

它會自己找出這台電腦已經有的 Codex 和 Claude Code，找到哪個就裝哪個；兩個都有就兩個都裝。你不用回答「我用哪個」。

只有當你是自己在終端機執行時，安裝程式才無法代替聊天視窗發話。這時關掉再重開你要用的 AI 工具，直接用白話說需求即可，例如：

```text
我想把客戶會議紀錄整理成待辦事項。
```

## 檢查更新

vv 不會在背景偷偷自己更新，因為它只是一組 `.md` 規則檔，不是 App。

但你可以請 Codex 或 Claude Code 幫你檢查 GitHub 上有沒有新版：

```text
vv 檢查更新
```

它會比對本機安裝版和 GitHub 公開包：

- GitHub 公開包：`https://github.com/vivi911/vv-conductor-public`
- 本機安裝的 skill：Codex 是 `~/.codex/skills/vv-conductor/`，Claude Code 是 `~/.claude/skills/vv-conductor/`
- 版本檔：repo 根目錄的 `VERSION`，以及安裝後那個資料夾裡的 `VERSION`

如果 GitHub 有新版，就要重新下載 repo，並覆蓋本機 skill。只看 GitHub 有更新還不夠，因為 AI 真正讀的是你電腦裡那個資料夾。

## 更新 vv

新版出來時，直接再跑一次同一行；它會更新公開包，再覆蓋這台電腦已偵測到的 AI 工具。

```bash
curl -fsSL https://raw.githubusercontent.com/vivi911/vv-conductor-public/main/install.sh | bash
```

AI 實際讀的是 `~/.codex/skills/vv-conductor/`（Claude Code 是 `~/.claude/skills/vv-conductor/`）裡的檔案。只把 repo 拉成最新、沒有覆蓋本機 skill 的話，新對話還是會一直跑舊版。

如果你不確定自己是不是最新版，直接問：

```text
vv 檢查更新
```

## 手動使用方式

如果你不想裝 skill，也可以純手動用。先把 `指揮家.md` 複製到你的 home 目錄：

```bash
cp ~/vv-conductor-public/指揮家.md ~/指揮家.md
```

再把 `memory-templates/` 複製到你固定放 AI 記憶的地方。

```bash
mkdir -p ~/vv-memory
cp ~/vv-conductor-public/memory-templates/*.md ~/vv-memory/
```

之後在 AI 對話框開頭貼：

```text
請先讀 ~/指揮家.md 和 onboarding.md，進入 AI 陪跑教練模式。現在直接問第 1 題，一次只問一題；第 7 題答完後，再開始我選的第一件小事。
```

## 第一次要做什麼

如果是 Codex 或 Claude Code 在目前對話幫你安裝，它會在檢查完檔案後直接打開 `onboarding.md`，一題一題問 7 題。你不用關掉對話，也不用再輸入任何啟動詞。

回答完後，把答案整理進：

- `memory-templates/01_我是誰.md`
- `memory-templates/02_專案範本.md`
- `memory-templates/03_給AI的工作規則.md`

不需要一次寫很完美。你回答完一題，vv 再問下一題；第 7 題就是第一件小事，答完後立刻開工。

## 你可以怎麼叫 vv

```text
vv
vv 我今天該先做什麼？
vv 幫我把這個需求拆成能施工的卡片。
vv 先讀我的 memory，再判斷這件事該不該做。
vv 幫我看這個專案現在卡在哪。
vv 這件事能不能自動跑？還是要我拍板？
vv 檢查更新
```

如果你剛安裝完，不知道從哪裡開始，也可以直接問：

```text
vv 可以幫我什麼？
你可以幫我什麼？
vv 怎麼使用？
怎麼用這套 AI 陪跑教練？
有哪些情境可以用？
我現在有點亂，vv 你建議我怎麼開始？
```

這些問法會讓 vv 先用白話跟你說明它能做什麼，而不是立刻要你看懂所有檔案。

## 常見使用情境

### 1. 新對話開場：先叫 `vv`，再說事情

第一次安裝完會自動問第 1 題。以後你打開一個新的 Codex 或 Claude Code 對話，可以這樣打：

```text
vv，我想做 XXX。
```

vv 會先去抓你的全域記憶入口，例如 Vault、`memory-templates/`、專案 `HANDOFF-LATEST.md`，找出你最近在做什麼、哪些專案還沒收尾、哪些地方需要你拍板。

如果你是第一次安裝、還沒建立 Vault，AI 陪跑教練會在安裝完後直接自我介紹，再用 7 題建立第一版 Vault。第 7 題會接上你的第一個小任務；這一次不用再打 `vv`。

如果記憶有接上，它會接著最新進度跟你聊。如果你本來有記憶、這次卻讀不到，它會明講「我現在讀不到記憶」，不會假裝知道。

### 2. 早上不知道先做什麼

```text
vv 我今天該先做什麼？
```

vv 會用老闆視角幫你看：哪件事最急、哪件事會卡錢或客戶、哪個專案被放太久、今天最值得先推哪一件。它不會把所有選項丟回給你自己選，而是會先給一個推薦。

### 3. 想法很亂，還不能施工

```text
vv 幫我把這個想法整理成可以動工的計畫。
```

vv 會先幫你拆成需求、卡點、完成條件和驗收方式。如果需要，它會用 PM、架構師、UX、開發、測試、發布這些角色 agent，逐步把模糊想法理順。

### 4. 要判斷 AI 能不能自動做

```text
vv 這件事能不能自動跑？還是要我拍板？
```

vv 會用紅黃綠規則幫你判斷：純整理、改文件、跑本機測試通常可以自動做；發送訊息、正式上線、金流、刪資料、OAuth、key rotation 這些高風險事會停下來問你。

### 5. 專案做到一半，想接回來

```text
vv 幫我看這個專案現在卡在哪。
```

vv 會先找 handoff 或專案記憶，幫你整理目前做到哪、真的接上了什麼、哪些還是待補、下一步最適合先做什麼。這就是這包最重要的用途：讓 AI 記得你們一起做過什麼，不用每次重新講一遍。

## 檔案結構

```text
vv-conductor-public/
├── README.md
├── VERSION
├── skill-index.md
├── 指揮家.md
├── vv-老闆視角.md
├── onboarding.md
├── memory-templates/
│   ├── 00_索引.md
│   ├── 01_我是誰.md
│   ├── 02_專案範本.md
│   └── 03_給AI的工作規則.md
└── skills/
    └── vv-conductor/
        ├── SKILL.md
        ├── VERSION
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── memory-template-guide.md
            ├── beginner-safety-start.md
            ├── package-maintenance.md
            └── vv-conductor-reference.md
```

## 這包現在分三層

### 1. 人看的公開文件

- `README.md`
- `VERSION`
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
- `skills/vv-conductor/VERSION`
- `skills/vv-conductor/agents/openai.yaml`
- `skills/vv-conductor/references/*.md`
