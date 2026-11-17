---
brand_id: algorithm-pipeline
kind: brand
summary: 算法与流水线技术对比风格 (科技风格默认模板) — 深度学习流水线、算法演进对比、端到端数据时序流、系统架构、工程对比分析
primary_color: "#0070C0"
secondary_color: "#2E7D32"
is_tech_default: true
---

# Algorithm Pipeline Brand Specification (算法与流水线技术对比规范)

> 科技风格默认模板 (Default Tech Brand Preset)。专注于计算机视觉、深度学习算法、端到端系统架构、工程流水线对比的高信息密度视觉规范。
> 核心原则：内容驱动图形表达、严禁纯文本卡片、实体图示与中间特征态呈现、工程级尺寸与闭环几何逆变换标注。

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Algorithm Pipeline Tech (算法与流水线技术对比风格) |
| Use Cases | 深度学习算法演进对比、图像与感知数据预处理/推理流、系统时序与数据流转、复杂工程方案多维对比评审、端到端闭环架构分享 |
| Tone | 严谨硬核、工程师视角、高信息密度、逻辑闭环、直观可解释 (White-box Visuals) |
| Core Metaphor | 双轨流水线对比 (Dual-Track Pipeline)、胶囊药丸标题栏 (Capsule Badge)、中间特征态 (Artifact Visuals)、逆变换对齐 (Inverse Transformation Loop) |

---

## II. Color Scheme

### 1. 基础与背景色彩

| Role | HEX | Color Name | Purpose |
|---|---|---|---|
| **Background** | `#FFFFFF` | Pure White | 页面主背景，极简通透底色 |
| **Canvas Secondary** | `#F8FAFC` | Light Slate | 页面次要区域、底衬与边距背景 |
| **Text Primary** | `#1A1A2E` | Deep Tech Black | 主标题、流程步骤、正文字体，高对比保证清晰度 |
| **Text Secondary** | `#5A6A7A` | Cool Gray | 补充说明、参数说明、次级标签 |
| **Text Muted** | `#8A95A5` | Slate Muted | 页脚、版本号、不可见辅助网格线 |

### 2. 双轨方案对比主色 (Dual-Scheme Dominant Colors)

| Role | HEX | Light Tint (Bg) | Border HEX | Purpose |
|---|---|---|---|---|
| **Scheme A (基准/经典方案)** | `#0070C0` (科技蓝) | `#EBF5FB` | `#90CAF9` | 经典算法、SAM 1 流程、基线链路、主控流程标题胶囊与主要箭头 |
| **Scheme B (演进/对比方案)** | `#2E7D32` (工程绿) | `#E8F5E9` | `#A5D6A7` | 演进算法、SAM 2.1 流程、升级版数据链路、优化路径标题胶囊与流向箭头 |

### 3. 多维功能与辅助语义色 (Semantic Accent Colors)

| Role | HEX | Light Tint (Bg) | Usage |
|---|---|---|---|
| **Math / Coordinate Mapping** | `#C2185B` (树莓红/粉) | `#FCE4EC` | 坐标变换公式、缩放比例推导、中心点映射计算卡片（支持粉红虚线框） |
| **Dimension Comparison Table** | `#FF9800` (暖橙/琥珀) | `#FFF3E0` | 方案核心差异对比表格表头、斑马纹高亮、核心参数差异列 |
| **Key Notices / Constraints** | `#7B1FA2` (紫罗兰/深紫) | `#F3E5F5` | 关键工程说明、部署约束、前置条件与边界警示卡片 |
| **Alert / Crop Padding** | `#E53935` (警示鲜红) | `#FFEBEE` | 填充区域裁剪红虚线框（Padding/Unpad）、异常拦截、硬性错误 |

---

## III. Typography & Font Stacks

| Role | Family Stack | Size & Weight | Notes |
|---|---|---|---|
| **Pill Badges (胶囊标题)** | `"PingFang SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif` | 18–22px, Bold (700), 白色文字 | 居中或左靠，深色胶囊内无衬线字 |
| **Step Headers (步骤标题)** | `"PingFang SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif` | 15–17px, Bold (600), `#1A1A2E` | 格式：`1. 阶段名称` |
| **Resolution / Dimensions** | `"Consolas", "Courier New", "Liberation Mono", monospace` | 13–15px, Regular (400), `#37474F` | 格式：`1280 × 720 (16:9)`，等宽字体 |
| **Math Formula (数学推导)** | `"Consolas", "Noto Sans Mono", monospace, "PingFang SC"` | 13–14px, Regular/Bold, `#C2185B` | 格式：`x' = 640 × 1024 / 1280 = 512` |
| **Body & Descriptions** | `"PingFang SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif` | 13–15px, Regular (400), `#333333` | 紧凑行距，行长不超过 35 中文字符 |

---

## IV. Core Visual Structures & Grammar (核心图形排版范式)

### 1. 胶囊药丸标题栏 (Capsule Badge Header)
- 必须使用深色高对比圆角矩形：`rx="18" ry="18" height="36"` 或 `rx="20" ry="20" height="40"`。
- 背景直接使用方案主色（如方案 A `#0070C0`，方案 B `#2E7D32`）。
- 文本使用纯白 `#FFFFFF` 加粗无衬线字体，垂直绝对居中，两端预留 $\ge 20\text{px}$ 留白。

### 2. 双大圆角流水线容器 (Dual-Track Pipeline Cards)
- 页面核心区域采用垂直排列的两大卡片（上下双轨，或左右并列）：
  - 外层矩形：`rx="12" ry="12"`，描边 `1.5px`，底色填充浅色 Tint（`#EBF5FB` 或 `#E8F5E9`）。
  - 内嵌 5–8 个有序处理阶段（从输入图像 $\to$ 预处理 $\to$ 特征提取 $\to$ 解码 $\to$ 上采样 $\to$ 逆变换对齐 $\to$ 最终输出）。
  - 阶段之间使用实体扁平箭头（Arrow）连接（宽度 16–24px）。

### 3. 实体图像与特征中间态 (No Pure Text, Visible Artifacts)
- **拒绝抽象文字占位**：必须展示真实的中间态视觉。
  - 原始输入：真实场景图像（带有等宽分辨率与宽高比标注）。
  - 填充阶段（Padding）：展示带有网格线（Grid Lines）的补零区域，标注填充像素高/宽（如 `↕ 448 像素`）。
  - 编码器（Encoder）：使用**梯形多边形（Trapezoid）**，左宽右窄，直观表达特征下采样与抽象。
  - 解码器（Decoder）：使用**倒梯形多边形**或矩形，右侧输出低分辨率 Logits 灰度模糊态（如 `256 × 256`）。
  - 逆变换还原（Unpad & Unscale）：展示红色虚线裁剪框剔除填充区，双线性插值扩展至原始比例。
  - 最终预测：生成高对比二值化 Mask（黑底白目标，`Logits > 0`）。

### 4. 闭环逆变换对齐折线 (Closed-loop Inverse Alignment Loop)
- 在流水线下方绘制大跨度 U 型双折线回溯箭头（Bottom Loop Wire）。
- 起点锚定在**预处理（Padding/缩放阶段）**，终点锚定在**逆变换对齐阶段（Unpad/Unscale）**。
- 箭头折线中段悬浮一个浅色半透明胶囊说明框（如 `完整的仿射几何逆变换 (Unpad + Unscale) 确保 Mask 与原图 100% 像素级对齐`），直观体现端到端像素闭环保证。

### 5. 底部三列沉淀区 (Bottom Tri-Column Analysis Section)
在主流水线下方，固定布局三列紧凑分析卡片（高 140–180px）：
1. **左列：坐标映射与数学推导 (Formula Deduction)**
   - 浅粉背景 `#FCE4EC`，可搭配细虚线红/粉边框 `#F48FB1`。
   - 标注原图坐标、缩放公式、归一化缩放因子与最终映射中心点。
2. **中列：多维核心差异对比表 (Structured Comparison Table)**
   - 暖橙色表头 `#FF9800`，白字；
   - 包含 `对比项`、`方案 A (典型实现)`、`方案 B (默认实现)` 三列；
   - 逐行对比缩放方式、是否 Padding、是否 Unscale、内容是否形变、输出 Mask 精度。
3. **右列：关键工程说明与注意事项 (Critical Notes Card)**
   - 浅紫背景 `#F3E5F5`，紫罗兰细边框 `#CE93D8`，紫色小标题；
   - 条列 1、2、3 项工程部署约束（如点云对齐、相机畸变校正、多传感器时序同步要求）。

---

## V. Voice & Tone
- **语言原则**：严格执行 **Chinese-First Presentation**，除专用算子（`Padding`、`Unpad`、`Unscale`、`Encoder`、`Decoder`、`Logits`、`Mask`）外，所有大标题、阶段名、图例、说明文字一律采用规范工程中文。
- **叙事逻辑**：结论先行、数学精确、标明单位与分辨率、具备物理可解释性。

## VI. Icon & Diagram Style
- **几何结构**：优先使用纯矢量 SVG 多边形（`polygon`、`rect`、`path`、`line`），带清晰的标尺与箭头。
- **虚线强调**：关键裁剪范围、预测边界、几何对应关系统一采用红色或对比色虚线（`stroke-dasharray="4,4"`）。
