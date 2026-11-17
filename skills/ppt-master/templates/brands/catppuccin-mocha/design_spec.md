---
brand_id: catppuccin-mocha
kind: brand
summary: Catppuccin Mocha 极客深色高对比度风 — 深邃炭青黑底、清爽低饱和粉彩对比、代码与架构极度清晰，适合开发者大会、AI技术汇报、系统架构设计
primary_color: "#89B4FA"
---

# Catppuccin Mocha 品牌规范 (Brand Specification)

> 纯视觉与调色规范预设 (Identity-only Preset)。无预设 SVG 页面骨架，执行者在全局色彩与排版规则下自由布局页面。

---

## I. 品牌定位与概述 (Brand Overview)

| 属性 | 设定值 |
|---|---|
| **品牌名称** | Catppuccin Mocha (摩卡) |
| **视觉风格** | 极客深色、现代科技感、低饱和粉彩高光、柔和护眼 |
| **适用场景** | 开发者大会/技术峰会、系统架构设计与演进、AI / 算法模型汇报、代码与技术方案评审 |
| **设计调性** | 硬核专业、极简沉稳、层次分明、极客工程师美学 |

---

## II. 色彩规范 (Color Scheme)

### 1. 核心调色板

| 角色 (Role) | HEX 颜色值 | 来源 (Provenance) | 语义说明 |
|---|---|---|---|
| **bg (画布背景)** | `#1E1E2E` | fact (Base) | 深邃夜色炭青背景，深沉且不刺眼 |
| **surface (主卡片背景)** | `#313244` | fact (Surface0) | 主卡片底板，与 Base 形成清晰的明暗层级 |
| **surface-subtle (嵌套容器)** | `#181825` | fact (Mantle) | 嵌套参数框、代码片段背板（比 Surface0 更深，形成内凹质感） |
| **surface-elevated (悬浮高亮)** | `#45475A` | fact (Surface1) | 选中卡片、重点对比容器、浮层背景 |
| **border (边框与分割线)** | `#45475A` | fact (Surface1) | 1px 细线边框，分割结构但不喧宾夺主 |
| **border-active (高亮边框)** | `#89B4FA` | fact (Blue) | 重点卡片的外发光或激活边框 |
| **text (主标题与正文)** | `#CDD6F4` | fact (Text) | 柔和浅青白主文字，最高对比度且无刺目炫光 |
| **muted-text (说明文字)** | `#A6ADC8` | fact (Subtext0) | 注释说明、次级指标、图表刻度 |
| **primary (品牌主色)** | `#89B4FA` | fact (Blue) | 标题关键词高亮、主折线、核心网络节点 |
| **secondary-accent (副主色)** | `#74C7EC` | fact (Sapphire) | 架构分层标识、次要流程分支 |
| **accent (高光强调)** | `#CBA6F7` | fact (Mauve) | 核心指标徽章、AI 算法锚点、架构中枢 |
| **success (成功/积极)** | `#A6E3A1` | fact (Green) | 性能提升、通过测试、吞吐量增长 |
| **warning (注意/预警)** | `#FAB387` | fact (Peach) | 延迟预警、待办事项、过渡状态 |
| **danger (危险/风险)** | `#F38BA8` | fact (Red) | 错误状态、性能瓶颈、架构单点故障 |

### 2. 颜色搭配原则
- **暗色对比度安全**：严格使用 `#CDD6F4`（Text）作为卡片内主文字，严禁在暗底上直接堆叠低明度暗字。
- **内凹代码块设计**：代码框与 JSON 数据块容器背景采用 `#181825`（Mantle），搭配 `#A6E3A1`（Green）或 `#89B4FA`（Blue）作为高亮符号。

---

## III. 字体排印规范 (Typography)

| 角色 | 推荐字体族 (Font Stack) | 字重 | 建议尺寸 |
|---|---|---|---|
| **Title (标题)** | `"Jellee", "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif` | 700 (Bold) | 封面 48-56px，内页标题 30-36px |
| **Body (正文)** | `"PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif` | 400 (Regular) | 正文 16-18px，卡片内 14-16px |
| **Annotation (注释)**| `"PingFang SC", "Microsoft YaHei", sans-serif` | 400 (Regular) | 12-14px |
| **Code / Monospace**| `Consolas, "Fira Code", "Courier New", monospace` | 500 (Medium) | 13-15px |

---

## IV. 图标风格 (Icon Style)

- **主选库**：`templates/icons/tabler-outline/`（深色背景下细线线性质感最佳）
- **备选库**：`templates/icons/chunk-filled/`（实体几何风）
- **图标颜色**：采用 `#89B4FA`（Blue）或 `#CBA6F7`（Mauve），增强暗色画面的精致感。

---

## V. 语气与调性 (Voice & Tone)

- **语言风格**：极客硬核、技术导向、量化准确。
- **架构表达**：推崇“组件分层 + 时序因果”，严禁模糊定性描述，优先列出 QPS、P99、内存开销等实测数据。

---

## VI. 卡片与容器原则 (Card & Layout Principles)

1. **暗底物理层次**：画布（`#1E1E2E`） < 主卡片（`#313244`） < 悬停强调（`#45475A`）；代码/数据子容器向下内凹（`#181825`）。
2. **多列防碰撞**：指标栏与并列卡片保持 $\ge 24\text{px}$ 安全边距，每行文字字符严格预算。
3. **单色微光效果**：重点卡片可使用带有极细弱 stroke 的描边（如 `stroke="#89B4FA" stroke-width="1.5"`）来形成视觉落点。
