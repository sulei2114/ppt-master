---
description: Generate publication-grade academic architecture and methodology pipeline diagrams (Figure 1) from paper text, incorporating PaperBanana planning and critic mechanisms.
---

# Academic Figure & Pipeline Workflow (PaperBanana Powered)

> **Role invoked**: [Academic_Planner](../references/academic-figure-planner.md) + [Executor](../references/executor-base.md) + [Academic_Critic](../scripts/academic_diagram_critic.py)

Dedicated standalone workflow for creating camera-ready, top-tier conference diagrams (Figure 1, Overview Architecture, Methodology Pipeline) suitable for venues like NeurIPS, ICML, CVPR, ICLR, and ACL.

> **Why this workflow?** Traditional slide generation formats content into multiple transition slides and card grids. This workflow focuses on **high-density, single-canvas academic diagrams** with deep methodology deconstruction, visual metaphor planning, orthogonal capsule routing, and multi-modal peer reviewer critique loops.

---

## Process Overview

```
Input (Method Text + Caption)
  │
  ▼
[Phase 1: Academic Planner] ──> Three-Domain Deconstruction + Metaphor Planning
  │
  ▼
[Phase 2: Canvas & Spec Lock] ──> Select Aspect Ratio (21:9 / 16:9 / 4:3) + Algorithm Pipeline Palette
  │
  ▼
[Phase 3: Native SVG Execution] ──> Rounded Domain Containers (rx="12") + Orthogonal Capsules + LaTeX Math
  │
  ▼
[Phase 4: Dual-Track Quality Check]
  ├─ Track A: Code Geometry & Collision Audit (svg_quality_checker & fireworks_bridge)
  └─ Track B: Peer Reviewer VLM Critique (academic_diagram_critic.py)
  │
  ▼ (Optional Polish Loop: up to 3 rounds)
  │
[Phase 5: Multi-Format Delivery]
  ├─ Camera-ready Vector SVG & High-res PNG (for LaTeX paper submission)
  └─ Editable PPTX (for manual drag-and-drop tweaks)
```

---

## Phase 1: Academic Planner (Methodology Deconstruction)

🚧 **GATE**: User has provided the paper's Methodology section / technical algorithm description and the intended Figure Caption.

### Step 1.1: Three-Domain Logical Extraction
Parse the input text into three physical domains (refer to [`references/academic-figure-planner.md`](../references/academic-figure-planner.md)):
1. **Input & Context Domain (01 输入与环境域)**: Inputs $X$, Prompts, Task definitions, Retrieval databases/memory.
2. **Core Processing & Evolution Domain (02 核心算法与交互演化中枢)**: Neural backbones, Attention modules, Agents, State machines, Latent transformations.
3. **Validation Gate & Admission Domain (03 确定性校验与准入决策)**: Evaluation environment, Loss functions ($\mathcal{L}$), Validation Gate ($\Delta \ge \theta$), Dual branching (Commit / Rollback).

### Step 1.2: Visual Metaphor Selection
Select an organizing visual metaphor based on algorithm characteristics:
- *Feature aggregation*: Funnel & Basin (流水汇聚漏斗)
- *Gating / MoE*: Routing Switch with probability capsules (自适应分流阀门)
- *Agent / Self-Reflection*: Dual-track loop with U-turn feedback (正交环形回路)
- *Memory / Knowledge retrieval*: Indexed Cylinder / Drawer (分层索引卡槽)

**✅ Checkpoint — Present the deconstructed 3-domain structure and chosen metaphor to the user before generating the SVG.**

---

## Phase 2: Canvas & Visual Spec Lock

### Step 2.1: Aspect Ratio Selection
Choose the canvas dimensions matching the target paper layout:
- **`figure-wide` (21:9 / 16:7 — e.g., 1280 × 550)**: Ideal for two-column paper top span (Figure 1 spanning both columns).
- **`figure-std` (16:9 — 1280 × 720)**: Ideal for comprehensive framework overview or presentation slide dual-use.
- **`figure-col` (4:3 — 960 × 720)**: Ideal for single-column compact pipeline.

### Step 2.2: Style & Color Lock
Default to **算法与流水线技术对比风格 (Algorithm Pipeline)**:
- Canvas: Pure white `#FFFFFF` (mandatory for academic submissions).
- Domain Containers: Soft cool grey (`#F8FAFC`), Ice blue (`#EFF6FF`), Pale green (`#F0FDF4`).
- Accent Colors: Tech Blue `#0284C7` (Forward flow), Forest Green `#16A34A` (Pass/Commit), Crimson `#DC2626` (Loss/Rollback).
- Font Stack: Declare cross-platform CJK stack (`WenQuanYi Micro Hei`, `Noto Sans CJK SC`, `PingFang SC`, `sans-serif`).

---

## Phase 3: Native SVG Execution

Executor constructs the standalone SVG following strict academic standards:
1. **Domain Containers**:
   ```xml
   <rect x="40" y="100" width="360" height="560" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
   <rect x="56" y="116" width="160" height="28" rx="14" fill="#0F172A"/>
   <text x="136" y="135" text-anchor="middle" font-size="12" font-weight="700" fill="#FFFFFF">01 输入与环境域</text>
   ```
2. **Orthogonal Connectors with Action Capsules**:
   - Must specify `stroke-linejoin="round"`.
   - Mid-line floating white pills with action verbs (`<rect rx="10" fill="#FFFFFF" stroke="#CBD5E1"/>`).
3. **Formula Rendering**:
   - For complex mathematical formulas ($\mathcal{L}_{task}$, $\theta$, $\mathbb{E}_{x \sim p}$), invoke `python3 scripts/latex_render.py` to generate clean vector/PNG formula assets and embed via `<image href="..."/>`.
4. **Icons**:
   - Leverage vector icons from `templates/icons/` to symbolize databases, encoders, models, and metric gauges.

---

## Phase 4: Dual-Track Quality Check & Polish Loop

### Track A: Code Geometry & Anti-Collision Check
Run the native geometry checkers:
```bash
python3 scripts/svg_quality_checker.py <diagram.svg>
python3 scripts/fireworks_bridge.py check <diagram.svg>
```
Verify zero text overflow, zero box collision, and correct CJK font stack declarations.

### Track B: Peer Reviewer VLM Critique (PaperBanana Powered)
Run the academic critic tool:
```bash
python3 scripts/academic_diagram_critic.py <diagram.svg> \
    --methodology "<method_text>" \
    --caption "<caption_text>" \
    --output "<project_dir>/critic_report.json"
```

The critic audits:
- **Faithfulness**: Zero hallucination, accurate data direction, no scope deviation.
- **Conciseness**: High visual SNR, no text paragraph dumping.
- **Readability**: Clear left-to-right flow, orthogonal lines, no overlapping.
- **Aesthetics**: Clean 3-domain boundaries, top-tier conference polish.

### Polish Loop:
If `passed: false` in `critic_report.json`:
- Read `actionable_revisions` from the report.
- Main agent performs precise coordinate/style edits on the SVG.
- Re-run verification (up to 3 iterations) until `passed: true`.

---

## Phase 5: Multi-Format Delivery

Export final deliverables for academic writing and presentations:
1. **Vector SVG & High-Resolution PNG**:
   - Primary deliverables for inclusion in LaTeX documents and paper drafts.
2. **Editable PPTX**:
   ```bash
   python3 scripts/svg_to_pptx.py <diagram.svg> -o <project_dir>/PPT/<diagram_name>.pptx
   ```
   Generates a fully editable slide with ungroupable shapes and text blocks, enabling authors to manually adjust layout, tweak node positions, or change text directly in PowerPoint/Keynote.
