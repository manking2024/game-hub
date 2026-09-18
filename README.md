# GameHub 在线小游戏站

GitHub Pages 主站 + Blogger 引流，双平台内容分发。纯静态、数据驱动、零成本。

## 目录结构

```
game-hub/
├── data/games.json        ← 唯一的编辑入口：游戏数据（名称/嵌入URL/原创内容/FAQ）
├── tools/gen_site.py      ← 生成器：读 games.json → 生成全部页面
├── assets/style.css       ← 站点样式（响应式）
├── blogger/post-template.html ← Blogger 引流发文模板
├── index.html             ← 首页（生成产物）
├── games/<slug>.html      ← 每款游戏一页（生成产物，含 Article/FAQPage Schema）
├── sitemap.xml            ← 站点地图（生成产物，提交 Search Console）
└── robots.txt             ← 允许抓取（生成产物）
```

## 日常发布流程（每上线一款游戏）

1. **注册游戏平台**：在 GameMonetize / GamePix / Poki 任选注册，挑一款游戏，复制 iframe 嵌入代码
2. **填数据**：把游戏信息填入 `data/games.json`（嵌入 URL、原创介绍、FAQ——内容可用 geo-content-optimizer 技能产出）
3. **生成**：`python tools/gen_site.py`
4. **发布**：`git add . && git commit -m "add: 新游戏" && git push`
5. **引流**：用 `blogger/post-template.html` 在 Blogger 发一篇带主站链接的短文

## 首次部署（一次性，约 20 分钟）

### 1. GitHub Pages 主站
1. 在 GitHub 新建公开仓库（如 `game-hub`），把本目录内容 push 上去
2. 仓库 Settings → Pages → Source 选 **Deploy from a branch** → 分支选 `main` → 根目录 `/`
3. 等 1-2 分钟，站点出现在 `https://<用户名>.github.io/game-hub/`
4. （推荐）绑定自定义域名：Settings → Pages → Custom domain 填你的域名，并按提示在 DNS 加 CNAME 记录

### 2. Search Console 收录
1. 打开 Google Search Console → 添加资源 → 域名类型，填你的域名
2. 按提示在 DNS 加 TXT 验证记录
3. 左侧 Sitemaps → 提交 `https://<你的域名>/sitemap.xml`

### 3. Blogger 引流渠道
1. 用 Google 账号开通 Blogger，起一个与站点相关的名字（如 "GameHub Games"）
2. 设置里把语言设为英文或按目标用户设置
3. 每款游戏发一篇 `blogger/post-template.html` 的短文，链接指向主站游戏页
4. （可选）Blogger 设置 → 自定义域名，指向同一域名子域（如 `blog.your-domain.com`）——不绑也能用 blogspot 子域

### 4. 游戏平台注册
1. 打开 GameMonetize / GamePix / Poki 的 publisher 页面注册
2. 通过审核后，在游戏库复制嵌入代码，填入 `data/games.json` 的 `embed_url`
3. 注意各平台条款：遵守流量质量要求，不刷量；分成比例 GameMonetize/GamePix 为 45%，Poki 自带流量 100%

## 政策提醒（务必遵守）

- **内容原创**：每个游戏页必须配原创介绍/玩法/FAQ，禁止纯 iframe 列表页（GitHub 条款打击低质 SEO 内容）
- **宣传话术**：避开"快速致富/躺赚"类表述（GitHub ToS 点名禁止）
- **游戏合规**：只嵌平台授权分发的游戏，不自行嵌入来源不明的内容
- **广告合规**：游戏内广告由平台控制；不要在页面上额外堆违规广告

## 账号管理（游戏站 manking2024 / 导航站 chuangyeli）

本机 gh 已登录两个账号，push 身份跟随当前 active 账号：

```powershell
gh auth status                          # 查看所有账号与当前 active
gh auth switch --user manking2024       # 更新游戏站前切到游戏站账号
gh auth switch --user chuangyeli        # 更新导航站前切回导航站账号
```

注意：git 代理已配置为系统代理 `127.0.0.1:7890`；若代理端口变化需同步修改
`git config --global http.proxy` / `https.proxy`。

## 与 geo-content-optimizer 技能配合

游戏页就是内容页，每款游戏按 GEO 四步走：
1. 用 gap 分析查"该游戏+玩法"的竞品缺口
2. 产出原创介绍 + 6 条以内 FAQ → 填入 games.json
3. Schema 由 gen_site.py 自动生成（Article + FAQPage）
4. 定期用 Search Console 看展示量与排名（AI 展示量在"搜索展示"维度看）
