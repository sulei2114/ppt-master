# Academic Figure & Methodology Planner

> **Role invoked**: Planner & Visual Stylist for Top-tier Conference Figures (NeurIPS, ICML, CVPR, ICLR, ACL).
> **Purpose**: Deconstruct complex academic methodology text, plan visual metaphors, establish rigorous topological flow, and guide high-fidelity SVG/PPTX authoring.

---

## 1. 核心解构方法：三域拆解法 (Three-Domain Methodology Deconstruction)

学术论文的方法章节（Methodology Section）通常信息密度极高，包含符号、算法、公式和多模块交互。严禁将其简单平铺为若干等大的方块卡片。必须按照顶会 Figure 1 的金标准，将其重构为三大逻辑物理域（Domain Containers）：

```
┌─────────────────────────┬───────────────────────────────────┬─────────────────────────┐
│  01 输入与环境域        │  02 核心算法与交互演化中枢        │  03 验证门禁与准入决策域 │
│  (Input & Context)      │  (Core Mechanism & Pipeline)      │  (Validation & Decision)│
│                         │                                   │                         │
│ · 原始输入数据 (X, Y)   │ · 特征提取 / 编码 (Backbone)      │ · 确定性校验器 / Loss   │
│ · 提示词 / 任务指令     │ · 交互网络 / 状态机 / 注意力      │ · 判定阈值 Δ ≥ θ ?      │
│ · 检索证据 / 历史轨迹   │ · 知识编辑 / 潜空间流转           │ · 分支: 合并通过 / 回滚 │
└─────────────────────────┴───────────────────────────────────┴─────────────────────────┘
            │                                                               ▲
            └─────────────────────── 闭环反馈回折链路 ───────────────────────┘
```

### 1.1 域 01：输入与问题域 (Input & Problem Domain)
* **包含要素**：原始输入数据、自然语言 Prompt、历史交互轨迹（Trace）、外部知识库（RAG/Memory）、待处理工况或环境状态。
* **视觉容器**：浅冷蓝或柔灰底色（`#F1F5F9` 或 `#EFF6FF`），细灰色边框（`stroke="#CBD5E1"`），圆角 `rx="12"`。
* **头部标识**：左上角悬浮深色胶囊徽标（如 `01 输入与问题上下文`）。

### 1.2 域 02：核心处理与交互演化域 (Core Processing & Interaction Domain)
* **包含要素**：多智能体交互网络、模型骨架（Encoder/Decoder/Diffusion）、注意力机制、中间潜变量分布、知识编辑/融合模块。
* **视觉容器**：纯净高光白底（`#FFFFFF`）配合细边框与微阴影，内部各子模块卡片横向或垂直对齐排布，层级清晰。
* **头部标识**：左上角深蓝胶囊徽标（如 `02 核心算法与多角色交互中枢`）。

### 1.3 域 03：验证门禁与准入决策域 (Validation Gate & Admission Domain)
* **包含要素**：验证环境、确定性评估器、损失函数计算（$\mathcal{L}_{task}$、$\mathcal{L}_{align}$）、判定门禁（$\Delta \ge \theta$ ?）及多分支决策。
* **视觉容器**：浅微绿或浅琥珀衬底（`#F0FDF4` 或 `#FEF3C7`），突出收益与判定结果。
* **头部标识**：左上角翠绿胶囊徽标（如 `03 确定性校验与准入决策`）。

---

## 2. 视觉隐喻规划 (Visual Metaphor Mode)

将高度抽象的数学算法转化为一眼看懂的直观视觉隐喻（Metaphor），提升审稿人的阅读愉悦感与理解效率：

| 算法/机制类型 | 推荐视觉隐喻 (Metaphor) | 构图拓扑特征 |
| :--- | :--- | :--- |
| **多模态/多特征融合** | **流水汇聚漏斗 (Funnel & Basin)** | 上方多分支并行下沉，经收窄漏斗统一投影到共享潜空间 |
| **门控/路由机制 (MoE)** | **自适应分流阀门 (Routing Switch)** | 菱形/圆角胶囊分流中枢，带概率权重胶囊标签引向不同专家块 |
| **多智能体演化/反思** | **双轨正交环形回路 (Feedback Loop)** | 前向推理主轴（实线科技蓝）+ 反思回滚大 U 型逆向走线（红色虚线） |
| **检索增强与长期记忆** | **圆柱体抽屉/索引卡槽 (Memory Cylinder)** | 立体圆柱或分层抽屉结构，带检索探针与 Top-K 匹配高亮 |
| **分层推理/分治决策** | **金字塔/阶梯递进 (Hierarchical Pyramid)** | 粗粒度语义（底层）$\to$ 细粒度操作指令（顶层）逐层聚焦 |
| **对比学习/双生网络** | **双子对称镜像轨 (Dual-Track Mirror)** | 上下或左右平行双轨，中间通过对比损失 $\mathcal{L}_{contrast}$ 弹性弹簧连线 |

---

## 3. 连线与交互语义规范 (Orthogonal Routing & Action Labels)

1. **绝对正交走线**：
   * 所有跨域连线严禁斜线穿插，必须采用**水平/垂直正交折线**（`stroke-linejoin="round"`）。
   * 主干前向数据流采用实线深灰或科技蓝（`#0284C7`，`stroke-width="2"`）。
   * 逆向反思、梯度更新或损失回传采用虚线红/橙（`stroke-dasharray="5 4"`）。
2. **悬浮行为胶囊 (Action Capsules)**：
   * 在连线中段必须悬浮白色微胶囊药丸，标注明确的动作协议动词：
     ```xml
     <!-- 折线 -->
     <path d="M 400 320 H 450 V 380 H 490" fill="none" stroke="#64748B" stroke-width="2" stroke-linejoin="round" marker-end="url(#arrow)"/>
     <!-- 悬浮动词胶囊 -->
     <rect x="420" y="340" width="76" height="20" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
     <text x="458" y="354" text-anchor="middle" font-size="10" font-weight="600" fill="#334155">提交候选修改</text>
     ```
3. **判定门禁双向分支**：
   * 成功分支（绿色向下/向右）：`<path stroke="#16A34A" ... />` $\to$ `准入/生效`
   * 失败分支（红色大 U 型回环）：向上方或下方走线通道反向回折至演化节点。

---

## 4. 色彩与中文字体标准 (Top-Tier Palette & Typography)

1. **学术背景与容器基调**：
   * 整体底板：纯白 `#FFFFFF`，杜绝黑色或深色背景（学术论文黑底极易拒稿）。
   * 容器衬底：柔灰 `#F8FAFC`、冰蓝 `#EFF6FF`、淡草绿 `#F0FDF4`、浅琥珀 `#FEF3C7`。
   * 强调饱和度控制：严禁大面积霓虹荧光色；关键高亮仅用于 Loss、门禁结果和最终交付产物。
2. **中文字体跨平台声明**：
   * 图内所有文本必须使用中文地道专业术语，且字体栈必须完整声明：
     ```css
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "WenQuanYi Micro Hei", "Noto Sans CJK SC", "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
     ```
