# Premium Visual Language: Diagrams, Tables, and Color

Use this reference for every deck, regardless of executor style. The target is the clear, restrained visual grammar common to strong ChatGPT-generated diagrams and tables: meaning is immediately legible, decoration stays quiet, and repeated elements feel intentional. It is not a fixed brand theme; follow the project's `spec_lock.md` tokens.

## 1. Shared design principles

- Give every page one visual job and one primary takeaway. Make that takeaway the strongest element through position, size, weight, or a restrained accent.
- Prefer whitespace, alignment, type scale, and subtle separators over nested boxes, heavy borders, gradients, and shadows.
- Use a card only when it groups a meaningful unit. Do not place every item in a separate card by default.
- Keep peer elements visually equal. Reserve stronger fill, contrast, or weight for the selected, exceptional, starting, decision, or outcome element.
- Use one icon style and consistent connector, corner, line, and spacing treatments throughout the deck.
- Keep diagrams and tables editable as SVG primitives and text where practical. Do not use an image to imitate structured information.

## 2. Color roles and restraint

Use the colors already locked in `spec_lock.md`; this file defines roles, not extra hex values. If the palette does not define a semantic color, ask Strategist to lock one before using it across pages.

| Role | Default use |
|---|---|
| Canvas / surface | Quiet light or dark neutral field from the locked palette; preserve strong text contrast |
| Primary text | Titles, key values, and the most important labels |
| Secondary text | Supporting explanation, units, captions, and metadata |
| Structure | Low-contrast separators, axes, gridlines, and connector lines |
| Accent | One primary highlight for the page's key point, active path, or selected data series |
| Semantic | Success, caution, and failure only when the meaning is genuinely semantic and the tokens are locked |

Color rules:

- Treat 60–30–10 as a wardrobe-like balance: about 60% neutral base (canvas and open space), 30% supporting color or tonal variation, and no more than 10% accent. It is a visual proportion, not a demand to fill the page with colored shapes.
- Let value contrast do most of the hierarchy work. A saturated hue should not become the largest surface by default; use it for a focal region, key path, or data point.
- Keep one dominant accent per page. Add another data-series color only when separate series must be compared; reuse the same mapping across the deck.
- Do not rely on color alone to convey state or category. Pair it with a label, shape, position, or line style.
- Use pale tints for grouping and selection; keep borders and gridlines quieter than content.
- Check text/background contrast and ensure muted labels remain readable at presentation size.
- Never invent new colors during page execution; update the design spec and `spec_lock.md` first if the existing palette cannot express the content.

### Wardrobe-inspired palette building

Apply the logic of a coordinated outfit to a deck: establish a calm base, choose colors that share a temperature and saturation character, then use one deliberate accent. The goal is harmony and hierarchy, not literal fashion imagery.

1. **Read temperature**: classify the intended neutrals and supporting hue as warm, cool, or near-neutral. Keep undertones coherent (for example, warm ivory with taupe/olive, or cool gray with slate/blue). Mix temperatures only when the contrast is deliberate.
2. **Set value before hue**: make sure the lightest and darkest roles are clear before adding color. Titles/body text must remain legible; vary lightness to separate layers instead of adding more hues.
3. **Choose one harmony**:
   - **Tonal** — one hue family in light, middle, and deep values. Quiet and cohesive; a good default for technical and analytical decks.
   - **Analogous** — neighboring hues, such as blue/teal or olive/sage. Let one lead and mute the others.
   - **Controlled complementary** — a restrained base plus a small contrasting accent (for example, navy with muted rust). Desaturate the accent and keep it sparse.
   - **Neutral with a jewel accent** — warm/cool neutrals with a deep burgundy, forest, or petrol accent for premium or editorial material.
4. **Preserve a supplied brand color**: keep its hue and any explicitly declared role/proportion intact. If the user specifies only a hue without saying how broadly to use it, build quiet neutrals around it and do not automatically spread it across the largest field.
5. **Avoid**: several unrelated saturated hues, accidental warm/cool clashes, equal-weight accents, defaulting to pure white plus bright corporate blue on every deck, and gradients used to disguise a weak palette.

When no color has been supplied, recommend one complete scheme with roles, temperature, harmony, and approximate 60–30–10 distribution. Offer alternatives only when the user asks or the content genuinely supports distinct directions.

### Example coordinated palettes

These are starting points for a new deck, not fixed themes. Adapt them to the content and lock only the chosen HEX values. In each palette, the pale base/support colors carry most filled areas; the deep anchor carries text and strong structure; the accent is used sparingly.

| Harmony | Base (~60%) | Support (~30%) | Deep anchor | Accent (≤10%) | Good fit |
|---|---|---|---|---|---|
| **Warm tailoring** | Warm ivory `#F4F0E8` | Stone `#D8D4C8` | Olive charcoal `#2F3531` | Muted leather `#94664A` | Business narrative, people, product, lifestyle |
| **Cool tailoring** | Mist `#F2F4F3` | Blue-gray `#CDD7D8` | Deep petrol `#2C4148` | Aged brass `#A07858` | Technology, architecture, modern service |
| **Ink and wine** | Paper `#F5F0EA` | Warm stone `#DED5CC` | Soft black `#302D30` | Burgundy `#794651` | Editorial, premium, heritage, leadership |

Use the deep anchor for body text rather than the pale support color. Accent colors should be checked against the actual background before using them for small text; if contrast is weak, use the deep anchor for the text and reserve the accent for a larger mark, rule, or tinted shape.

## 3. Flowcharts and process diagrams

First classify the relationship, then choose the simplest matching layout:

| Relationship | Preferred form |
|---|---|
| Short ordered process | Horizontal sequence with aligned steps |
| Many stages or long labels | Vertical sequence or a two-row serpentine path with an obvious continuation cue |
| Responsibility across teams/systems | Swimlanes with clear lane labels and limited crossings |
| Conditional logic | Decision diamond only at a real branch; label every outgoing path |
| Parallel work | Parallel branches that visibly converge only when the process truly converges |
| Time or version progression | Timeline with consistent date/phase markers |
| System structure | Layered or grouped architecture diagram, with direction shown only where data/control flows |

Construction rules:

- Use a restrained node grammar: rounded rectangle for an action, diamond for a condition, and a distinct but simple treatment for start/end. Avoid giving every node a unique shape.
- Align nodes to a clear grid; use consistent node sizes for peers and enough whitespace to separate stages.
- Use thin, consistent connectors with clear direction. Route lines through open corridors; avoid crossings, backtracking, and lines that pass through nodes or labels.
- Label branches near their outgoing connector (for example, “是/否” or “成功/失败”). Do not leave the reader to infer which path means what.
- Highlight only the current/critical path or the key decision. Keep secondary paths lower contrast while preserving legibility.
- Keep node text short and action-oriented. Move qualifications and implementation details to a note or adjacent explanation rather than shrinking labels.
- Avoid putting the whole diagram inside a decorative card. Use a light region boundary only when it clarifies a real subsystem or grouping.

## 4. Tables and comparison layouts

- Use a table when readers need to compare values across the same fields. If the content is mainly a sequence or causal relationship, use a diagram instead.
- Keep the header clear, align text left and numbers right, standardize units and decimal precision, and make row spacing generous enough for projection.
- Prefer horizontal row separators and whitespace over a full dark grid. Use vertical separators only where they materially improve scanning.
- Use a quiet header treatment, subtle alternating rows only for long tables, and a restrained tint or accent rule for at most one key row/column.
- Keep emphasis consistent: bold the key value or label, not every cell. Explain abbreviations and units in the header or a short note.
- Split a table across slides or convert it into a comparison when it needs tiny type, excessive wrapping, or too many columns. Preserve the comparison logic and label continuation pages clearly.
- Never use color as the sole indicator for better/worse; include signs, words, or symbols as well.

## 5. Charts, infographics, and default visual review

- Choose chart type from the question: trend → line; magnitude comparison → bar; composition → stacked bar or carefully limited donut; relationship → scatter; stages → process diagram. Avoid decorative 3D charts.
- Remove chart furniture that does not help read the data. Keep axes, labels, units, source, and uncertainty clear; directly label series when that is easier than a legend.
- An infographic should have a clear reading order and one synthesis statement. Icons are cues, not substitutes for labels or evidence.
- Vary page rhythm across the deck: alternate dense analytical pages with simpler explanation, comparison, or breathing pages. Do not repeat one grid pattern on every page.
- Before writing speaker notes, review each generated page for: one obvious takeaway; appropriate visual form; balanced whitespace; aligned peers; legible labels; restrained and consistent color; clear flow direction; and table/chart readability at presentation scale.
- Fix clear issues in the page SVG and rerun the technical checker. If improving the page would require changing the locked brand palette, content meaning, or approved structure, record the issue for Strategist instead of making an untracked design decision.

## 6. 算法与流水线技术对比范式 (Algorithm & Pipeline Comparison Paradigm)

针对深度学习、计算机视觉、端到端数据流水线与算法演进对比页面，强制遵循以下工业级图解规范：

- **胶囊药丸标题栏 (Capsule Badge Header)**：每个核心算法/处理流水线顶部使用深色高对比圆角矩形（`rx="18"`），采用白字加粗标明阶段主旨（如方案 A 科技蓝 `#0070C0`，方案 B 工程绿 `#2E7D32`）。
- **双轨容器与横向处理流 (Dual-Track Containers & Horizontal Flow)**：
  - 核心处理流封装在带大圆角（`rx="12"`）、浅色背景衬底（`#EBF5FB` / `#E8F5E9`）的大卡片中；
  - 内部按逻辑顺序水平排列 5–8 个紧凑处理步骤，各步骤之间使用平滑实心箭头（Arrow）连接；
  - 步骤统一具备双层标注：上标编号与中文阶段名（如 `1. 原始图像`），下标等宽格式分辨率/尺寸（如 `1280 × 720 (16:9)`、`1024 × 1024`）。
- **实体图像与特征中间态真实呈现 (Intermediate Feature Artifacts)**：
  - 严禁空洞的纯文本占位卡片；必须展示真实的中间态视觉（如缩放图像、带填充网格的补零区、特征图）；
  - 核心网络模块使用物理隐喻几何图形（如 Image Encoder 采用梯形 Trapezoid 表现特征下采样抽象，Decoder 采用倒梯形或低分 Logits 灰度态 `256 × 256`）；
  - 逆变换还原（Unpad & Unscale）必须展示红色虚线裁剪框剔除填充区，清晰呈现几何变换过程。
- **闭环逆变换对齐折线 (Closed-loop Inverse Alignment Arrows)**：
  - 在流水线下方使用大跨度 U 型双折线回溯箭头，将预处理端（缩放/Padding）与后处理对齐端（Unpad/Unscale）连接；
  - 折线中段悬浮浅色半透明胶囊说明框，注明数学几何逆变换依据（如“完整的仿射几何逆变换确保 Mask 与原图 100% 像素级对齐”）。
- **底部三列沉淀分析区 (Bottom Tri-Column Analysis Section)**：
  - 左列 [数学推导/坐标映射]：浅粉色卡片，清晰展示坐标换算公式（`x' = x * scale`）与推导结果；
  - 中列 [核心维度对比表]：暖橙色表头对比表格，针对缩放方式、是否 Padding、是否 Unscale、输出精度等逐行严谨对比；
  - 右列 [工程注意事项/约束]：淡紫色卡片，条列 1、2、3 项系统落地约束与边界条件。
- **全中文工程优先 (Chinese-First Presentation)**：除不可替代的算子专业名称（如 `Padding`、`Unpad`、`Mask`、`Logits`）外，所有大标题、图解说明、表头及注意事项全部强制使用规范、准确的中文。

## 7. 顶会科研论文关键图与架构演化范式 (Top-tier Academic Figure 1 & System Pipeline Paradigm)

针对人工智能、多智能体协作、机器人决策系统及前沿算法论文（如 KARMA、ATP、WeVisCut 等顶会架构与演化方法）的关键全景图（Figure 1 / Overview Architecture），强制遵循以下融合理念与设计规范（结合 `happy-figure`、`research-figure-pipeline` 与 `Cocoon-AI/architecture-diagram-generator`）：

### 7.1 黄金三段式域边界划分 (Three-Domain Partitioning)
画布主体必须清晰划分为三大功能域（Domain Containers），通过浅灰背景与细边框物理隔离，严禁无边界混乱拼贴：
1. **左域：输入与问题域 (Input & Problem Domain)**：
   - 容纳原始输入数据、业务工况、故障/失败轨迹证据（Failure Trace）或上下文知识库；
   - 容器样式：浅冷蓝或柔灰底色（`#F1F5F9` / `#EFF6FF`），细灰色虚线或实线边框（`stroke="#CBD5E1"`），圆角 `rx="12"`；
   - 域头部：左上角悬浮深色胶囊徽标（如 `01 输入与问题上下文`）。
2. **中域：核心处理与交互演化域 (Core Processing & Interaction Domain)**：
   - 容纳多智能体协作网络、模型骨架、知识原子化编辑模块（Atomic Knowledge Edits）或动态状态机；
   - 容器样式：高光白底（`#FFFFFF`）配合细边框与微阴影，内部各子模块卡片平铺排列，具备清晰的主从依赖；
   - 域头部：左上角深蓝胶囊徽标（如 `02 核心算法与多角色交互中枢`）。
3. **右域：验证门禁与准入决策域 (Validation Gate & Admission Domain)**：
   - 容纳确定性校验器、验证环境（Validation Environment）、准入阈值 $\theta$ 判定与双向分支；
   - 容器样式：浅琥珀/微绿衬底（`#F8FAFC` / `#F0FDF4`），展示指标收益判定结果；
   - 域头部：左上角翠绿胶囊徽标（如 `03 确定性校验与准入决策`）。

### 7.2 决策门禁与闭环反馈回环 (Decision Gate & Feedback Loops)
- **判定门禁 (Validation Gate)**：必须使用具有明确视觉隐喻的菱形或高对比胶囊判定框，清晰标注判定依据（如 `收益增益 Δ ≥ θ ?`）；
- **双向明确分支**：
  - **成功分支 (Success Path)**：向下或向右绿色加粗箭头（`stroke="#16A34A"`），直达 `保留并合并 (Commit & Merge)` / `任务准入`；
  - **失败分支 (Rollback Path)**：红色或橙色箭头（`stroke="#EF4444"`），直达 `拒绝并回滚 (Rollback)`；
- **跨域闭环反馈回折 (U-turn Feedback Routing)**：
  - 从失败端引出大跨度正交 U 型双折线回环箭头，跨越上方或下方走线通道回连至中域的“演化器/反思器”；
  - 连线采用平滑圆角（`stroke-linejoin="round"`），中段必须悬浮半透明胶囊说明框（如 `带失败证据与原因反思触发逆向重构`），严禁连线直接穿过文字。

### 7.3 正交连线与交互说明 (Orthogonal Routing & Action Labels)
- 连线严禁斜插或随意曲线，统一采用严格的**水平/垂直正交折线**；
- 所有跨模块连线上，必须在折线中段放置白色描边小药丸背景框（如 `<rect rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>`），标注明确的通信行为动词与协议契约（如 `提交候选原子修改`、`提取验证收据`、`广播状态快照`）。

### 7.4 学术配色与中文字体自适应 (Academic Palette & Cross-Platform CJK)
- **色系规约**：纯白底板（`#FFFFFF`），主干道采用科技冷灰（`#0F172A` / `#334155`），重点链路使用沉稳科技蓝（`#0284C7`），成功指示使用森林绿（`#16A34A`），警示/失败使用砖红（`#DC2626`）；
- **文字与多字体保证**：图内所有大标题、域名称、卡片标题、步骤及回环说明一律使用地道专业的中文；字体栈必须声明包含 `"WenQuanYi Micro Hei", "Noto Sans CJK SC", "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif`，确保无头 Chromium 和 Linux 渲染端输出平滑无方块。
