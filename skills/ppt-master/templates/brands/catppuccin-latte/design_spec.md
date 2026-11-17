---
brand_id: catppuccin-latte
kind: brand
summary: Catppuccin Latte 暖调浅色极简风 — 米白温暖底色、柔和对比度、温润粉彩强调色，适合技术白皮书、行业分析、高阶学术与咨询汇报
primary_color: "#1E66F5"
---

# Catppuccin Latte 品牌规范 (Brand Specification)

> 纯视觉与调色规范预设 (Identity-only Preset)。无预设 SVG 页面骨架，执行者在全局色彩与排版规则下自由布局页面。

---

## I. 品牌定位与概述 (Brand Overview)

| 属性 | 设定值 |
|---|---|
| **品牌名称** | Catppuccin Latte (拿铁) |
| **视觉风格** | 暖调浅色、极简纯粹、柔和不刺眼、高可读性 |
| **适用场景** | 技术方案白皮书、咨询行业汇报、学术研讨会、明亮环境现场演示 |
| **设计调性** | 严谨克制、现代温润、逻辑清晰、避免高饱和度荧光色彩 |

---

## II. 色彩规范 (Color Scheme)

### 1. 核心调色板

| 角色 (Role) | HEX 颜色值 | 来源 (Provenance) | 语义说明 |
|---|---|---|---|
| **bg (画布背景)** | `#EFF1F5` | fact (Base) | 温暖奶白色，消除纯白荧光带来的长时间视疲劳 |
| **surface (主卡片背景)** | `#FFFFFF` | approx | 纯白卡片，与奶白 Base 形成微妙温润的物理层级微对比 |
| **surface-subtle (嵌套卡片)** | `#E6E9EF` | fact (Mantle) | 嵌套参数框、次级容器、代码块浅色背板 |
| **border (边框与分割线)** | `#CCD0DA` | fact (Surface0) | 1px 细线边框、网格微弱分割线 |
| **text (主标题与正文)** | `#4C4F69` | fact (Text) | 深蓝灰主文字，对比度强且无纯黑生硬感 |
| **muted-text (说明文字)** | `#6C6F85` | fact (Subtext0) | 注释文字、次级指标、图表轴刻度 |
| **primary (品牌主色)** | `#1E66F5` | fact (Blue) | 页面标题重点词、主行动号召、关键图标、主折线 |
| **secondary-accent (副主色)** | `#7287FD` | fact (Lavender) | 流程辅助、次级节点、标签背板高亮 |
| **accent (高光强调)** | `#8838EF` | fact (Mauve) | 核心数据徽章、视觉锚点、特殊分类标签 |
| **success (成功/积极)** | `#40A02B` | fact (Green) | 正向增长率、成功状态、达标指示 |
| **warning (注意/预警)** | `#DF8E1D` | fact (Yellow) | 中性风险提示、进行中状态、边界条件 |
| **danger (危险/风险)** | `#D20F39` | fact (Red) | 关键故障、下降指标、阻碍因素 |

### 2. 颜色搭配原则
- **拒绝刺眼纯黑**：正文使用 `#4C4F69` 而非 `#000000`。
- **克制使用高光色**：单张幻灯片内的强调色不得超过 2 种（推荐以 Blue 为主，Green/Mauve 按语义点缀）。

---

## III. 字体排印规范 (Typography)

| 角色 | 推荐字体族 (Font Stack) | 字重 | 建议尺寸 |
|---|---|---|---|
| **Title (标题)** | `"Jellee", "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif` | 700 (Bold) | 封面 48-56px，内页标题 30-36px |
| **Body (正文)** | `"PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif` | 400 (Regular) | 正文 16-18px，卡片内 14-16px |
| **Annotation (注释)**| `"PingFang SC", "Microsoft YaHei", sans-serif` | 400 (Regular) | 12-14px |
| **Code / Data (代码/数据)**| `Consolas, "Courier New", monospace` | 500 (Medium) | 13-15px |

---

## IV. 图标风格 (Icon Style)

- **主选库**：`templates/icons/tabler-outline/`（简约线性几何风）
- **备选库**：`templates/icons/phosphor-duotone/`（双色微透明底衬风）
- **图标颜色**：跟随上下文文字颜色（`#4C4F69`）或主品牌色（`#1E66F5`）。

---

## V. 语气与调性 (Voice & Tone)

- **语言风格**：专业严谨、逻辑先导、结论前置。
- **标点与排版**：严格避免中英文标点混用，指标数字与单位之间保持半角空格（如 `99.8 %`、`120 ms`）。
- **表情符号 (Emoji)**：谨慎避免使用通俗表情，使用扁平矢量图标替代。

---

## VI. 卡片与容器原则 (Card & Layout Principles)

1. **容器圆角**：卡片使用 `rx="8"` 或 `rx="10"` 圆角矩形。
2. **多列防碰撞**：多列指标或并列卡片之间保持 $\ge 20\text{px}$ 间距，文字不触碰边框（内边距 $\ge 24\text{px}$）。
3. **嵌套代码框**：在卡片内展示代码或结构体时，使用 Mantle 背板（`#E6E9EF`）并包裹独立的 `rect` 容器。
