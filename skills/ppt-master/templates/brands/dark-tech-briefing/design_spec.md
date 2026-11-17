---
brand_id: dark-tech-briefing
kind: brand
summary: 深蓝灰暗调技术简报风格 (Dark Tech Briefing) — 现代暗色极客风、多Agent协作架构、系统联调排障、时序与工程闭环汇报
primary_color: "#55C6D8"
secondary_color: "#F5A15D"
background_theme: dark
---

# Dark Tech Briefing Brand Specification (深蓝灰暗调技术简报规范)

> Identity-only preset. 提取自实战技术简报与多Agent系统联调实战架构。
> 核心视觉特征：现代深邃蓝灰底色、高饱和荧光青蓝流程导向、琥珀暖橙决策点高亮、步骤数字徽章、暗色多面板卡片容器。

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Dark Tech Briefing (深蓝灰暗调技术简报) |
| Use Cases | 多Agent协作系统架构、系统故障排查与3D定界、端到端时序与闭环链路、高阶开发者技术简报、现代暗色控制台风格汇报 |
| Tone | 严谨克制 (Restrained)、工程沉浸感 (Deep Tech)、架构结构化 (Structured Vector)、证据驱动 (Evidence-Led) |
| Core Metaphor | 数字圆标步骤徽章 (Numbered Circle Badges)、青蓝流程导向箭头 (Cyan Flow Connectors)、暗色微卡片网格 (Dark Panel Grid) |

---

## II. Color Scheme

### 1. 基础表面与背景色 (Dark Surface Hierarchy)

| Role | HEX | Color Name | Purpose |
|---|---|---|---|
| **Background** | `#101923` | Deep Blue-Gray | 页面主背景，深邃暗调科技底色 |
| **Secondary bg** | `#192734` | Midnight Slate | 核心容器卡片、流程步骤面板底色 |
| **Border** | `#354756` | Steel Border | 卡片边框（1.5px~2px），保证暗色界线清晰而不刺眼 |
| **Accent bg** | `#30271F` | Dark Amber Tint | 特殊高亮/评估/决策步骤的警示底衬卡片 |

### 2. 文本与排版对比色 (Text Palette)

| Role | HEX | Purpose |
|---|---|---|
| **Text Primary** | `#F2F5F8` | 主标题、卡片粗体标题、核心结论白字 |
| **Text Secondary** | `#B3C1CC` | 步骤说明文字、副标题、正文描述 |
| **Text Muted** | `#8193A2` | 阶段小标头、辅助说明、页脚标签 |

### 3. 功能与语义高亮色 (Functional Accents)

| Role | HEX | Color Name | Purpose |
|---|---|---|---|
| **Primary** | `#55C6D8` | Cyan Glow (青蓝) | 主流程箭头、当前阶段圆标高亮、核心操作节点、主类别标签 |
| **Accent** | `#F5A15D` | Amber Coral (琥珀橙) | 评估节点、决策分流、根因报警、关键质量门禁 |
| **Secondary Accent** | `#8AA8C0` | Slate Blue (灰蓝) | 次级步骤圆标底衬、辅助连接线、信息透视卡片 |
| **Success** | `#62C89A` | Mint Green (薄荷绿) | 终态闭环、测试通过、经验沉淀、正常服务指示灯 |

---

## III. Typography & Font Stacks

| Role | Family Stack | Size & Weight |
|---|---|---|
| **Category Tag** | `"PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif` | 13–15px, Bold (700), 大写或带分隔符，`#55C6D8` |
| **Slide Title** | `"PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif` | 32–36px, Bold (700), `#F2F5F8` |
| **Slide Subtitle** | `"PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif` | 20–24px, Regular (400), `#B3C1CC` |
| **Card Header** | `"PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif` | 16–18px, Bold (700), `#F2F5F8` |
| **Step Number Badge** | `"Consolas", "PingFang SC", monospace` | 12–13px, Bold (700), 居中于圆标内 |
| **Body / Details** | `"PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif` | 12–14px, Regular (400), `#B3C1CC` |

---

## IV. Core Visual Grammar & Layout Patterns (排版范式)

### 1. 顶部技术摘要区 (Header Anchor)
- 左上方设置两级标题：
  - 上标小字分类（如 `多Agent协作系统  /  真机联调排障`，`#55C6D8` 字色）；
  - 主标题粗体白字（`#F2F5F8`，字号 34px）；
  - 副标题灰色解释（`#B3C1CC`，字号 23px）。
- 右侧预留技术插图或架构小徽标（`150 × 110 px` 矢量图或示意图），增强视觉焦点。

### 2. 水平带序号流程步进栏 (Numbered Step Ribbon)
- 包含 4–6 个圆角矩形步骤卡片（`rx="12" fill="#192734" stroke="#354756"`）；
- 每个卡片左上角附带**微型圆形数字徽标**：
  - 正常阶段：浅青蓝光晕圆框（`fill="#55C6D8" fill-opacity="0.15" stroke="#55C6D8"`）内写 `01`、`02`；
  - 核心评估阶段：琥珀橙色边框与文字（`#F5A15D`）；
- 步骤之间通过横向实体粗线与实心箭头无缝连接（`stroke="#55C6D8" stroke-width="3"`）。

### 3. 双列或三列暗色结构卡片 (Dark Multi-Column Grid)
- 下半部分布局若干独立的暗色大卡片（`fill="#192734" stroke="#354756" rx="12"`）；
- 内部采用结构化列表、代码片段块（带等宽字体）或微型时序分层图，高信息密度而不杂乱。

---

## V. Voice & Tone
- 极客视角、工程实践为准绳、强调端到端闭环与现场取证；
- 语言风格遵循中文优先原则，技术术语严谨规范。
