# AI 陪跑教練（vv）vv-pack-1.7.0

English version: [`../README.md`](../README.md)（repo 預設語言）

> 第一次先陪你安全完成一個小任務；之後再接上記憶、派工與驗收。

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

這套 AI 陪跑教練不是單純教你「怎麼問 AI」。第一次使用時，它會先問你想做什麼、講清楚真正風險、把任務縮成安全的第一版；等你完成第一件事後，再由你決定要不要建立長期記憶。

下載這包之後，你不是得到一個普通聊天提示詞，而是一套給 Codex 或 Claude Code 使用的安全開工、記憶、派工和驗收規則。

你可以叫它 `vv`，也可以叫它 `vivi`——兩個字效果完全一樣。**vv 就是你自己專屬的 AI 教練**——不是只有第一次才能用，以後每次打開新對話，打 `vv` 或 `vivi` 就能把他叫出來。他會先看你是誰、現在有哪些事在跑，再判斷這件事可以自動做，還是要先停下問你。

它有全域記憶，這個記憶庫就叫 **Vault**。你可以把自己的背景、專案狀態、工作禁區寫進 `~/vv-memory/`（也就是你的 Vault），讓 AI 記得你是誰、專案做到哪、之前跟你協作過什麼、哪些事不能亂碰。

一般 AI 像失憶症，每次開新對話都要你重講一遍自己是誰；Vault 就是讓 AI「記得你」的那個地方。Vault 是進階的長期陪跑功能，不是第一次開工前的考卷。建立後，每次打 `hi`、`vivi`、`vv` 或 `vv vault`，它會先讀 Vault，再接著上次的進度繼續。

它也有開機規則。以後你打開新對話，只要打 `vv` 或 `vivi`，它就會先抓最新事件和進度接著聊，不用每次重新交代「我是誰、上次做到哪、這個案子卡在哪」。

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
5. `skills/vv-conductor/memory-templates/`：把你的背景、專案、工作規則寫成 AI 看得懂的檔案。
6. `skills/vv-conductor/onboarding.md`：想讓 AI 長期記得你時，再用 7 題建立 memory。

## 平常對話怎麼用 vv（只要記得一個字：`vv` 或 `vivi`）

每次打開新對話，打 `vv` 或 `vivi` 就好——**不用另外記「第一次要打什麼」「想確認記憶要打什麼」，兩個字挑一個記住就夠**。只要你已經建過 Vault，它會自動先讀記憶，回你上次做到哪、下一步是什麼，手上還有哪些專案沒完成，不用你另外問。

```text
vv
```

```text
你回來了，上次做到 XX，下一步是 YY。你手上還有 [專案 A] 卡在 [下一步]、[專案 B] 還沒開始——要先接哪一個？
```

`hi`、`vivi`、`指揮家`、`AI 陪跑教練`、`vv vault` 這幾個字也都能叫醒他、效果完全一樣——只是備用說法，你不需要特地記，打 `vv` 或 `vivi` 就好。

叫醒之後，直接講你要幹嘛就行，例如：

```text
vv 我今天該先做什麼？
vv 幫我把這個想法拆成能施工的卡片。
vv 這件事能不能自動跑，還是要我拍板？
```

一句話：**開對話 → 打 `vv` 或 `vivi` → 講你要做的事**。不用背指令、不用寫複雜提示詞。

## v1.6 跟 v1.5 差在哪

| v1.5 | v1.6 |
|---|---|
| 重點在「執行規則」：任務分級、派工、紅黃綠授權、驗收、停損 | 加上「記憶入口」：先讓 AI 認識你，再開始安全做事 |
| AI 開工時主要讀 `指揮家.md` | AI 開工時先讀 memory 訊號，再讀 `指揮家.md` |
| 比較適合已經有固定工作流的人 | 更適合第一次導入 AI 工作中樞的人 |
| 進度靠 `HANDOFF-LATEST.md` 接棒 | 進度仍靠 handoff，但新增「老闆視角」幫你提醒被遺忘的案 |

一句話：

v1.5 是「AI 做事前的安全規則」。
vv-pack-1.7.0 是「先安全完成第一件事，再決定要不要讓 AI 長期認識你」。

## 這包適合誰

- 創業者、主管、顧問、自由工作者。
- 手上很多案子，常常忘記哪個做到哪。
- 想用 Claude Code、Codex 或其他 AI 幫忙拆任務、寫文件、寫 code、驗收成果。
- 不想每次都重新解釋自己的背景、規則、禁區。

## 先把這包下載到電腦

後面所有步驟都是從你電腦裡的這份副本出發，所以第一步先把它抓下來。

打開「終端機」（Terminal），把下面這段整段貼進去，按 Enter：

```bash
git clone https://github.com/vivi911/vv-conductor-public.git ~/vv-conductor-public
```

跑完之後，這包就在你的家目錄底下，路徑是 `~/vv-conductor-public`。`~` 就是你的個人資料夾，不用自己去找它在哪。

之後 README 裡所有指令都會用這個路徑，你直接照貼就好。如果你想放到別的地方，記得後面每一條指令的路徑也要跟著換。

想確認有沒有抓成功，貼這句，會列出這包的檔案：

```bash
ls ~/vv-conductor-public
```

## Codex / Claude Code 怎麼用

這包 Codex 和 Claude Code 都能用。安裝的是同一份 `vv-conductor` skill，只是放的資料夾名字不同。

差別不在能不能裝，而在你會拿它們做什麼。

### Codex：比較像會動手施工的工作台

Codex 適合拿來做：

- 讀 repo、改檔案、跑測試。
- 判斷紅黃綠授權，知道哪些事可以自動做、哪些事要先問你。
- 接手 `HANDOFF-LATEST.md`，不用每次重新交代專案進度。
- 把一個工程或文件任務拆成可驗收的步驟。

### Claude Code：比較像會陪你想清楚的策略室

Claude Code 適合拿來做：

- 幫你整理想法、寫文案、寫簡報、做策略推演。
- 用老闆視角幫你排優先順序。
- 依照你的 memory 和規則，延續同一套工作習慣。

AI 陪跑教練就是讓兩邊都照同一套工作規則跑。你兩邊都裝也完全沒問題，它們各自讀自己的資料夾，不會打架。

## 正式 Skill 安裝方式（Codex / Claude Code 二選一或都裝）

安裝之後，vv 才會變成一個固定的按鈕：你打 `hi`、`vivi`、`vv`、`指揮家`，它就自動讀這套規則，不用每次貼檔案。

兩邊裝法一模一樣，只有資料夾名字不同。你用哪個就貼哪一段。

### 如果你用 Codex

```bash
mkdir -p ~/.codex/skills
cp -R ~/vv-conductor-public/zh-TW/skills/vv-conductor ~/.codex/skills/
```

### 如果你用 Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R ~/vv-conductor-public/zh-TW/skills/vv-conductor ~/.claude/skills/
```

兩邊都用的話，兩段都貼，各裝各的不會打架。

裝完**重開** Codex 或 Claude Code，當你說 `hi`、`vivi`、`AI 陪跑教練`、`開工手冊`、`vv`、`指揮家`、`今天先做什麼`、`派工`、`紅黃綠` 或 `handoff`，它就會觸發這個 skill。

想確認有沒有裝好，貼這句（有列出檔案就是成功）：

```bash
ls ~/.codex/skills/vv-conductor    # 你用 Codex 的話
ls ~/.claude/skills/vv-conductor   # 你用 Claude Code 的話
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

新版出來時，兩步：先把 repo 拉成最新，再覆蓋本機安裝版。

```bash
cd ~/vv-conductor-public && git pull
```

```bash
cp -R ~/vv-conductor-public/zh-TW/skills/vv-conductor ~/.codex/skills/    # 你用 Codex 的話
cp -R ~/vv-conductor-public/zh-TW/skills/vv-conductor ~/.claude/skills/   # 你用 Claude Code 的話
```

AI 實際讀的是 `~/.codex/skills/vv-conductor/`（Claude Code 是 `~/.claude/skills/vv-conductor/`）裡的檔案。只把 repo 拉成最新、沒有覆蓋本機 skill 的話，新對話還是會一直跑舊版。

如果你不確定自己是不是最新版，直接問：

```text
vv 檢查更新
```

## 改這包之前（給想自己改的人）

這包的同一條規矩會寫在好幾個檔案裡：`SKILL.md` 給 AI 讀、`指揮家.md` 給人讀、
`onboarding.md` 是第一次使用的流程。**改其中一份、忘了另一份，規則就會互相矛盾，
而且不會有任何錯誤訊息**——AI 只是安靜地選到不一樣的做法。

所以改完一定要跑這個：

```bash
python3 ~/vv-conductor-public/scripts/check-consistency.py
```

它會掃全部規則檔，檢查跨檔規矩有沒有對不上、該留的東西有沒有被弄丟、檔案引用會不會
斷掉。不綠就不要發布。

## 手動使用方式

如果你不想裝 skill，也可以純手動用。先把 `指揮家.md` 複製到你的 home 目錄：

```bash
cp -n ~/vv-conductor-public/zh-TW/指揮家.md ~/指揮家.md
```

⚠️ **這個 `-n` 也不能拿掉。** 如果你電腦裡已經有一份 `~/指揮家.md`（例如你之前裝過、或自己改過），沒有 `-n` 會直接把它蓋掉。跳過不代表沒裝成功——是保護你原本那份不被覆蓋；如果你就是要換新版，先手動確認舊檔沒有你想留的東西，再自己刪舊檔重貼這行。

再把 `skills/vv-conductor/memory-templates/` 複製到你固定放 AI 記憶的地方。

```bash
mkdir -p ~/vv-memory
cp -n ~/vv-conductor-public/zh-TW/skills/vv-conductor/memory-templates/*.md ~/vv-memory/
```

⚠️ **那個 `-n` 不能拿掉。** 它的意思是「已經存在的檔案就跳過」。

`~/vv-memory/` 是**你自己**的記憶庫。沒有 `-n` 的話，你哪天再貼一次這行，空白原稿就會把你累積的內容整個蓋掉，而且救不回來。

之後要更新這包，**只要重裝 skill 就好，不用再碰這個資料夾**。

之後在 AI 對話框開頭貼：

```text
請先讀 ~/指揮家.md，進入 AI 陪跑教練模式。第一次先陪我安全完成一個小任務；我同意建立長期記憶後，再讀 ~/vv-memory/00_索引.md。
```

## 第一次要做什麼

安裝後開一個新對話，只要打：

```text
hi
```

AI 陪跑教練會先問：「你現在最想請 Codex 或 Claude Code 幫你做什麼？」接著幫你講清楚風險、縮成安全的第一版，不會先丟 7 題考卷。

完成第一個安全任務後，如果你希望它下次記得你的背景、進度和工作禁區，再回：

```text
幫我建立 Vault。
```

這時它才會打開 `onboarding.md`，一題一題問你 7 題。

回答完後，把答案整理進：

- `~/vv-memory/01_我是誰.md`
- `~/vv-memory/專案/<專案名>.md`（你提到的每個專案各自一份，複製自 `02_專案範本.md`，不要全部擠進同一個檔案）
- `~/vv-memory/03_給AI的工作規則.md`

不需要一次寫很完美。你回答完一題，vv 再問下一題；v1.6 的設計是先有一版，工作一週後再養。

## 你可以怎麼叫 vv

```text
hi
vv
vv vault
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

### 1. 新對話開場：直接打 `hi` 或 `vivi`

以後你打開一個新的 Codex 或 Claude Code 對話，可以先打：

```text
hi
```

（打 `vivi` 效果完全一樣。）

vv 會先去抓你的全域記憶入口，例如 Vault、`~/vv-memory/`、專案 `HANDOFF-LATEST.md`，找出你最近在做什麼、哪些專案還沒收尾、哪些地方需要你拍板。

如果你是第一次拉下這包、還沒建立 Vault，打 `hi` 或 `vivi` 不會報錯——AI 陪跑教練會先自我介紹，再問你想做什麼，陪你安全完成第一個小任務。只有你想要長期記憶時，才會再用 7 題建立第一版 Vault。

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
├── README.md                    ← 英文版（repo 預設語言）
├── skills/vv-conductor/         ← 英文版
└── zh-TW/                       ← 你現在看的這個中文版
    ├── README.md
    ├── VERSION
    ├── skill-index.md
    ├── 指揮家.md
    ├── vv-老闆視角.md
    └── skills/
        └── vv-conductor/
            ├── SKILL.md
            ├── VERSION
            ├── onboarding.md
            ├── agents/
            │   └── openai.yaml
            ├── memory-templates/
            │   ├── 00_索引.md
            │   ├── 01_我是誰.md
            │   ├── 02_專案範本.md
            │   └── 03_給AI的工作規則.md
            └── references/
                ├── memory-template-guide.md
                ├── beginner-safety-start.md
                ├── package-maintenance.md
                └── vv-conductor-reference.md
```

`onboarding.md` 和 `memory-templates/` 都放在 skill 資料夾裡面，這樣你安裝之後 AI 才找得到它們。安裝指令只複製 `zh-TW/skills/vv-conductor`，放在外面的東西不會被帶過去。

## 這包現在分三層

### 1. 人看的公開文件

- `README.md`
- `VERSION`
- `指揮家.md`
- `vv-老闆視角.md`

### 2. 記憶模板（空白原稿，跟著 skill 一起安裝）

- `skills/vv-conductor/memory-templates/00_索引.md`
- `skills/vv-conductor/memory-templates/01_我是誰.md`
- `skills/vv-conductor/memory-templates/02_專案範本.md`
- `skills/vv-conductor/memory-templates/03_給AI的工作規則.md`

這四份是**空白原稿**，永遠不要直接填在這裡——你更新這包的時候整個資料夾會被覆蓋。要用就先複製到你自己的記憶庫（預設 `~/vv-memory/`），填在那邊。

### 3. 正式 skill

- `skill-index.md`
- `skills/vv-conductor/SKILL.md`
- `skills/vv-conductor/VERSION`
- `skills/vv-conductor/onboarding.md`
- `skills/vv-conductor/agents/openai.yaml`
- `skills/vv-conductor/references/*.md`
