# html-anything-skills

Extracted skill templates from <https://github.com/nexu-io/html-anything> (Apache-2.0).
Only the reusable skill templates were kept — the Next.js app was discarded.

## How to use

Each folder is one skill: `SKILL.md` (frontmatter + layout brief, mostly Chinese) + `example.html` (self-contained: Tailwind Play CDN + Google Fonts only, double-click to open).
`_SHARED_DESIGN_DIRECTIVES.md` is the common preamble the original app prepends to every skill body before the user's content — world-class visual-designer rules, content-drives-page-count, single-file HTML output.

## Skills (81)

- **article-magazine** `article` — Substack / Medium 高级感长文排版, 适合公众号、博客发布
- **article-sketchnote-editorial** `article` — 把一个概念铸成杂志专题档案——真问题→失败→转折→顿悟→命名, 6 个 layout 模具 + 4 字族对比 + 探案档案细节
- **blog-post** `article` — 杂志感长文, 含 masthead、hero、figures、pull quote、作者署名
- **card-twitter** `card` — 推特金句 / 数据卡, 适合配推文
- **card-xiaohongshu** `card` — 小红书风格知识卡片, 多张联排可滑动浏览
- **competitive-teardown** `doc` — 定位图 + 功能矩阵 + 价格对比 + 机会窗口, 把竞品资料转成产品决策报告
- **dashboard** `dashboard` — 固定侧栏 + 顶栏 + KPI 网格 + 1-2 张图
- **data-report** `data` — 把 CSV/Excel/JSON 数据转成漂亮的可视化报告页
- **dating-web** `dashboard` — 消费感配对仪表板: 信号 ticker + KPI + 30 天柱状 + 趋势
- **deck-blueprint** `slides` — 奶油纸 + 锈红 + 蓝图网格 mask + 黑边硬卡片 + pipeline 盒
- **deck-course-module** `slides` — 暖纸背景 + Playfair, 左侧学习目标常驻, 含 MCQ 自测页
- **deck-dir-key-nav** `slides` — 8 页单色背景, 160px display + 4px accent + Mono 箭头列表
- **deck-graphify-dark** `slides` — 深夜渐变 + 漂浮 orbs + SVG 力导向图谱 + JetBrains Mono
- **deck-guizang-editorial** `slides` — 电子杂志 × 电子墨水; 10 个版面 + 5 套调色板 (墨水/靛蓝瓷/森林墨/牛皮纸/沙丘)
- **deck-hermes-cyber** `slides` — 黑底 + CRT 网格扫描线 + $ 命令行标题 + 薄荷绿大字 + 三档 tag
- **deck-ljg-present** `slides` — 把 outline 1:1 铸成色块大字宣言 deck, 原文不动只做美化。三档主题 black / red / yellow
- **deck-magazine-web** `slides` — 电子杂志 × 电子墨水风, WebGL 流体背景 + 衬线 display
- **deck-obsidian-claude** `slides` — GitHub-dark + 紫蓝环境光 + 三色渐变标题 + GitHub 风代码
- **deck-open-slide-canvas** `slides` — 锁死 1920×1080 画布, React 组件级自由组合, 不绑模板
- **deck-pitch** `slides` — 10 页融资 deck, 白底 + 蓝紫渐变 hero, traction 柱状, $X.XM ask
- **deck-presenter-mode** `slides` — tokyo-night 默认主题, T 切换 5 主题, S 打开提词器 popup
- **deck-product-launch** `slides` — 暗 hero + 亮内容, 橙→桃 accent, 特性卡 + 定价 + CTA
- **deck-replit** `slides` — Replit Slides 八套主题 (helix/holm/vance/bevel/world/atlas/bluehouse)
- **deck-safety-alert** `slides` — 红琥珀警示色 + hazard 条纹 + L1/L2/L3 tier 卡片 + 删除线标题
- **deck-simple** `slides` — 通用 horizontal-swipe HTML deck, 不要 magazine 调
- **deck-swiss-international** `slides` — 16 列网格 + 单一饱和 accent + 22 个锁死版面 (Klein Blue / Lemon / Mint / Safety Orange)
- **deck-tech-sharing** `slides` — GitHub-dark + JetBrains Mono + 终端代码块, 含 agenda + Q&A
- **deck-xhs-pastel** `slides` — 奶油底 + 柔光 blob + 马卡龙圆角卡片 + Playfair 斜体序号
- **deck-xhs-post** `slides` — 9 页 3:4 竖版图文, 暖 pastel + 虚线 sticker 卡片
- **deck-xhs-white** `slides` — 纯白 + 顶部彩虹 bar + 渐变文字 + 马卡龙软卡片 + 黑底 pill
- **digital-eguide** `article` — 两页跨页电子指南, 封面 + 课程页 + pull-quote + 步骤列表
- **doc-kami-parchment** `doc` — 暖羊皮纸底 (#f5f4ed) + 墨蓝单色 accent (#1B365D) + 单一衬线字体, 编辑级排印
- **docs-page** `doc` — 三栏文档页: 侧导航 + 正文 + 右 TOC
- **email-marketing** `email` — 产品发布邮件, 含 masthead、hero、CTA、规格表, table-fallback
- **eng-runbook** `doc` — 服务概述 + alerts 表 + dashboards + 操作命令 + on-call + 事故清单
- **exec-briefing-memo** `doc` — Decision needed + recommendation + evidence + tradeoffs, 把复杂材料压成可拍板的一页
- **experiment-readout** `data` — 假设 + 指标 + 结果 + 解释 + 决策, 把 A/B 或产品实验转成行动建议
- **finance-report** `finance` — Masthead + KPI + 收入/烧钱图 + P&L 表 + 重点 + 展望
- **flowai-team-dashboard** `dashboard` — 三个 tab 的团队管理后台: 成员、详情、活动日志, 含图表 + CSV 导出
- **frame-data-chart-nyt** `video` — NYT-newsroom 排版 + 错峰揭示动画 + 编辑级图表 (折线/柱/范围带)
- **frame-flowchart-sticky** `video` — SVG 曲线连接 + 便利贴节点 + 光标交互, 像白板 brainstorm
- **frame-glitch-title** `video` — 数字故障 / 像散偏移 / 数据腐败标题, 适合视频转场 / cyberpunk hero
- **frame-light-leak-cinema** `video` — 胶片漏光 + 颗粒噪点 + 16:9 letterbox + 衬线大字, 电影感开场 / 章节卡
- **frame-liquid-bg-hero** `poster` — WebGL 风流体置换背景 + 顶部叠加金句, 适合视频片头 / landing hero / 海报
- **frame-logo-outro** `video` — Logo 分块组装入场 + glow bloom + tagline 揭示, 适合视频片尾 / 品牌闭幕
- **frame-macos-notification** `card` — 拟真 macOS 通知 banner + app icon + 标题正文, 适合 video overlay / 产品发布预告
- **gamified-app** `mobile` — 三屏: 封面 / 今日任务带 XP / 任务详情, 暗色舞台
- **hr-onboarding** `doc` — 首周日程 + buddy + 学习路径 + 设备 + 完成标准
- **info-funnel** `data` — 3-6 阶递减漏斗, 突出转化率 / 筛选比例 / 流量损耗。竖图适合 IG Story / 小红书
- **invoice** `finance` — 标准发票: 寄件/收件 + 明细 + 税 + 总额 + 付款指引
- **kanban-board** `dashboard` — To do / In progress / In review / Done 四列, 卡片 + 头像 + 泳道
- **live-dashboard** `dashboard` — Notion 风团队仪表板, KPI + 7 日 sparkline + activity feed + 任务表
- **magazine-poster** `poster` — Sunday-paper 风格, 大字 serif headline + 双栏正文 + 编号 sections
- **meeting-notes** `doc` — 标题 + 出席 + 议程 + 决议 + action items + 下次
- **mobile-app** `mobile` — 像素级 iPhone 15 Pro 边框, 一屏 app 截图
- **mobile-onboarding** `mobile` — 三个手机框并排: splash / value-prop / sign-in
- **mockup-device-3d** `poster` — iPhone + MacBook 仿 GLTF 静态展架, 屏幕内嵌真实 HTML 内容, 玻璃镜头折射, 360° 转盘构图
- **motion-frames** `video` — 可循环 CSS 动效组合: 旋转环、地球仪、计时器、视差标签
- **pm-spec** `doc` — 问题 + 成功指标 + 范围 + user stories + 设计 + 发布 + 待解决
- **poster-hero** `poster` — 竖版海报 / 朋友圈分享图, 强视觉冲击
- **ppt-keynote** `slides` — 苹果 Keynote 级别幻灯片, 一屏一卡, 键盘左右切换
- **pricing-page** `prototype` — 三档定价 + 特性对比表 + FAQ
- **prototype-web** `prototype` — 可点击的功能性 Web 原型, 含导航、英雄区、特性区、CTA
- **resume-modern** `resume` — 现代极简简历, A4 单页, 适合打印或导出 PDF
- **saas-landing** `prototype` — 单页 SaaS 落地页, 含 hero/features/social-proof/pricing/CTA
- **social-carousel** `card` — 三张方形卡片轮播, 标题串联, 品牌 mark + 编号
- **social-media-dashboard** `dashboard` — 平台切换 + 粉丝/互动 KPI + 增长曲线 + Top post + 热门话题
- **social-media-matrix** `dashboard` — 电影感多平台社媒分析: 互动图、悬浮洞察、区间对比、明暗主题
- **social-reddit-card** `card` — 拟真 Reddit 帖子卡 + 上下投票 + 评论数, 适合视频叠加 / 故事分享
- **social-spotify-card** `card` — Spotify Now Playing 风格卡: 专辑封面 + 进度条 + 播放控制, 适配视频叠加 / 个人主页
- **social-x-post-card** `card` — 拟真 X 推文卡片 + 互动数据 (likes/reposts/views), 适配视频叠加或图卡分享
- **sprite-animation** `poster` — 像素美术 + kinetic 字体的解说帧, 纯 CSS 循环, 可录视频
- **team-okrs** `dashboard` — 季度 banner + 3 个目标 + KR 进度条 + owner + 状态 pill
- **vfx-text-cursor** `video` — 光标拖光 + 彩色像散射线 + 定向光斑, 适合视频片头逐字揭示金句
- **video-hyperframes** `video` — Hyperframes / Remotion 兼容的连续帧动画, 可自动播放
- **waitlist-page** `prototype` — 极简产品预发布落地页, 含邮箱捕获、logo、装饰图层
- **web-proto-brutalist** `prototype` — Swiss industrial-print 风: 单字 grotesque、巨数字、ASCII 装饰
- **web-proto-editorial** `prototype` — Editorial-minimalist: 暖色单色 canvas + serif display + grotesque body
- **web-proto-soft** `prototype` — Apple 调: 银/奶 canvas + 双层斜面卡片 + button-in-button + spring
- **weekly-update** `slides` — 6-8 页横向滑动周报: 已发布 / 进行中 / 阻塞 / 指标 / 求助
- **wireframe-sketch** `prototype` — 网格背景 + marker 笔触 + 多 tab + sticky note + scribble 图表
