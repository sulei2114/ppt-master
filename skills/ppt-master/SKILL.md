---
name: ppt-master
description: >
  AI-driven multi-format SVG content generation system. Converts source documents
  (PDF/DOCX/URL/Markdown) into high-quality SVG pages and exports to PPTX through
  multi-role collaboration. Also creates top-tier academic paper architecture diagrams (Figure 1)
  and methodology pipelines (PaperBanana powered). Use when user asks to "create PPT", "make presentation",
  "生成PPT", "做PPT", "制作演示文稿", "学术架构图", "论文Figure 1", "画架构图", or mentions "ppt-master".
---

# PPT Master Skill

> AI-driven multi-format SVG content generation system. Converts source documents into high-quality SVG pages through multi-role collaboration and exports to PPTX.

**Core Pipeline**: `Source Document → Create Project → [Template] → Strategist → [Image_Generator] → Executor Live Preview → Quality Check → Post-processing → Export`

> [!CAUTION]
> ## 🚨 Global Execution Discipline (MANDATORY)
>
> **This workflow is a strict serial pipeline. The following rules have the highest priority — violating any one of them constitutes execution failure:**
>
> 1. **SERIAL EXECUTION** — Steps MUST be executed in order; the output of each step is the input for the next. Non-BLOCKING adjacent steps may proceed continuously once prerequisites are met, without waiting for the user to say "continue"
> 2. **BLOCKING = HARD STOP** — Steps marked ⛔ BLOCKING require a full stop; the AI MUST wait for an explicit user response before proceeding and MUST NOT make any decisions on behalf of the user
> 3. **NO CROSS-PHASE BUNDLING** — Cross-phase bundling is FORBIDDEN. (Note: the Eight Confirmations in Step 4 are ⛔ BLOCKING — the AI MUST present recommendations and wait for explicit user confirmation before proceeding. Once the user confirms, all subsequent non-BLOCKING steps — design spec output, SVG generation, speaker notes, and post-processing — may proceed automatically without further user confirmation)
> 4. **GATE BEFORE ENTRY** — Each Step has prerequisites (🚧 GATE) listed at the top; these MUST be verified before starting that Step
> 5. **NO SPECULATIVE EXECUTION** — "Pre-preparing" content for subsequent Steps is FORBIDDEN (e.g., writing SVG code during the Strategist phase)
> 6. **NO SUB-AGENT SVG GENERATION** — Executor Step 6 SVG generation is context-dependent and MUST be completed by the current main agent end-to-end. Delegating page SVG generation to sub-agents is FORBIDDEN
> 7. **SEQUENTIAL PAGE GENERATION ONLY** — In Executor Step 6, after the global design context is confirmed, SVG pages MUST be generated sequentially page by page in one continuous pass. Grouped page batches (for example, 5 pages at a time) are FORBIDDEN
> 8. **SPEC_LOCK RE-READ PER PAGE** — Before generating each SVG page, Executor MUST `read_file <project_path>/spec_lock.md`. All colors / fonts / icons / images MUST come from this file — no values from memory or invented on the fly. Executor MUST also look up the current page's `page_rhythm` (`anchor` / `dense` / `breathing`), `page_layouts` (which template SVG to inherit, if any), and `page_charts` (which chart template to adapt, if any). Empty / absent entries are intentional Strategist signals — see executor-base.md §2.1. This rule exists to resist context-compression drift on long decks and to break the uniform "every page is a card grid" default
> 9. **SVG MUST BE HAND-WRITTEN, NOT SCRIPT-GENERATED** — Every SVG page is written by the main agent directly, one page at a time (see rules 6 and 7). Writing or running a Python / Node / shell script that produces the SVG files in batch — looping over pages, templating from data, or emitting them via a generator — is FORBIDDEN, including under "save tokens", "quick draft", or "user is in a hurry" pretexts. The script-generation path was tried on a feature branch and abandoned: cross-page visual consistency depends on per-page authoring with full upstream context, which a generator script cannot reproduce
> 10. **SINGLE LATEST PPTX ARTIFACT DISCIPLINE (同一PPT单最新版本留存硬约束)** — 同一个 PPT 项目在导出与重新构建时，**有且仅保留最新的一份 PPTX 制品**。在执行 Step 7.3 或应用注解重新导出时，必须输出为规范命名的 `<project_path>/PPT/<project_name>.pptx`，严禁在同一个项目下持续堆积带有不同时间戳的多个历史陈旧 `.pptx` 文件。重新导出或二次生成时，必须直接覆盖或清理该项目旧版本的 `.pptx`，确保 `<project_path>/PPT/` 目录下始终仅存在最新一份最终交付物。
> 11. **TEXT & CODE BLOCK OVERFLOW DISCIPLINE (文本与代码块严禁溢出硬约束)** — In SVG, `<text>` nodes do NOT auto-wrap. Every text line, card parameter, and code/JSON snippet MUST be strictly budgeted against container width:
>     - **No Inline Label + Complex Data**: NEVER place a Chinese label and a structured dictionary/array on the same single `<text>` line (e.g. `· 动作序列: actions: [...]` will inevitably overflow 544px containers). The label and the data payload MUST be separated into distinct vertical lines.
>     - **Dedicated Nested Code Box**: For any code or JSON payload exceeding 40 characters, ALWAYS create a nested `<rect>` sub-box (e.g. height 42–60px, width `container_width - 40px`) and format the payload across indented multi-lines (`< 45` characters per line).
>     - **Hard Character Limits per Line**: In a 544px card, CJK text MUST NOT exceed 35 characters/line, monospace code MUST NOT exceed 50 characters/line; in a 380px card, CJK MUST NOT exceed 24 characters/line, monospace MUST NOT exceed 34 characters/line. Violating this will trigger overflow defects.
> 12. **CJK FONT RENDERING & LINUX COMPATIBILITY (中文字体跨平台与Linux渲染兼容规范)** — When declaring font stacks for Chinese/CJK content or monospace code blocks, include pre-installed open-source CJK fonts (e.g. `"WenQuanYi Micro Hei"`, `"Noto Sans CJK SC"`, `"Source Han Sans SC"`, `"SimHei"`) alongside Windows/macOS fonts (`"PingFang SC"`, `"Microsoft YaHei"`, `"Consolas"`, `sans-serif`) to ensure headless renderers (CairoSVG, Chromium) and Linux preview servers render crisp CJK glyphs, symbols, and monospace code without tofu boxes or garbled text.
> 13. **CONTENT-LED VISUAL GRAMMAR (内容驱动的图形表达)** — Choose the visual form that best explains the content: process, comparison, hierarchy, timeline, data, or narrative. Do not default to card grids or add diagrams/images solely to fill space. Every visual element must clarify a relationship, support the page's main conclusion, or establish an intentional section mood. See `references/premium-visual-language.md` for the default flowchart, table, and color rules.
> 14. **MULTI-COLUMN METRICS & CARD ANTI-COLLISION DISCIPLINE (多列指标栏与卡片防碰撞硬约束)** — When laying out multi-column status bars, KPI metrics strips, or horizontal card decks, the AI MUST strictly enforce per-column text length budgeting and position isolation to eliminate cross-column character collision ("前后字体重合"):
>     - **Per-Column Character Budget**: In a 4-column strip (column width ~260–290px), text per line MUST NOT exceed 16 CJK characters (or 26 Latin characters); in a 3-column strip (~360–390px), max 22 CJK characters; in a 2-column card (~550–580px), max 34 CJK characters. A minimum safety margin of $\ge 25\text{px}$ before any divider line or card border is MANDATORY.
>     - **No Unanchored Inline Overlap (禁止无坐标保护的内联文本叠加)**: In multi-column metric bars or cards, when displaying Label + Value pairs with distinct styles/colors, DO NOT rely on raw consecutive `<tspan>` tags without explicit coordinates. The AI MUST either format them as a single concatenated text string or separate them into distinct `<text>` elements with explicit, deterministic `x` coordinates (e.g. `Label: x=24`, `Value: x=110`) to eliminate cross-platform tspan text overlap risks.
> 15. **CACHE-BUSTING & LIVE PREVIEW FRESHNESS DISCIPLINE (动态预览防强缓存与资源指纹硬约束)** — Browser caching can silently serve stale assets (e.g. returning HTTP 304 Not Modified for unchanged filenames like `image.png`), misleading users into believing feedback was not applied:
>     - **Asset Path Versioning / Cache Busting (资源修改必更名)**: Whenever an image, diagram, or asset is modified, regenerated, or cleaned up in response to user feedback, the AI MUST rename or version the asset file (e.g. `images/<name>_v2.png` or `images/<name>_updated.png`) and update the SVG `<image href="...">` reference accordingly. NEVER overwrite an asset in place while keeping the exact same filename in the SVG.
>     - **No-Store Server Headers**: All preview endpoints (`/`, `/api/*`, `/images/*`) MUST include `Cache-Control: no-store, no-cache, must-revalidate, max-age=0` and `Pragma: no-cache` headers to prevent stale 304 responses in user browsers.
> 16. **MANDATORY VISUAL ANCHORS & NO PURE TEXT (严禁纯文本排版与图片强制写入硬约束)** — 严禁全纯文本卡片或缺乏视觉图象的大段文字堆砌。幻灯片中不能仅有纯文本，必须包含高质量的图片/视觉锚点（`<image href="...">`），如架构拓扑、交互时序、数据流转图、AI技术概念图或系统实体插图。页面必须图文结合、信息密度与视觉吸引力兼具，彻底杜绝单调枯燥的“纯文本PPT”。
> 17. **CHINESE-FIRST PRESENTATION DISCIPLINE (生成PPT极力减少英文与尽可能使用中文硬约束)** — 生成 PPT 时必须最大限度减少英文词汇，除纯代码变量、专用协议名（如 `navigate_to_charge`、`navigation`、`ToolMessage`）或无公认中文对照的纯英文技术缩写外，所有大标题、副标题、标签、卡片标题、流程阶段、说明文本及图表文字**必须优先并且强制使用地道、专业的中文**，严禁使用非必要的中英双语夹杂或英文大写副标（如严禁滥用 `SYMPTOM & PHENOMENON`、`WHY IT ESCAPED`、`FEEDBACK ARCHITECTURE` 等英文占位），确保页面以中文为主、表意精准通透。
> 18. **TOP-TIER ACADEMIC FIGURE & SYSTEM PIPELINE DISCIPLINE (顶会科研论文架构图与闭环演化范式)** — 当页面表达技术方案、模型架构、算法演化或论文解读等复杂系统时，严格遵循学术关键图（Figure 1）三大原则：
>     - **三段式结构转译 (happy-figure 范式)**：强制拆解为 `输入与问题域` → `核心处理与交互演化域` → `验证门禁与准入域`，层次分明，绝不画无边界的平铺方块。
>     - **两阶段门禁控制 (research-figure-pipeline 范式)**：进入执行前，必须先在规划/确认阶段对齐全局概念 Master 架构（域边界、模块职责、数据流向），再进行模块化矢量组装。
>     - **原生 SVG 矢量容器与正交闭环 (Cocoon-AI & fireworks 规范)**：必须采用浅灰/冷调带标圆角容器（`rx="12"`）清晰隔离各域；连线采用带圆角的正交折线（`stroke-linejoin="round"`），并在折线中段悬浮浅色胶囊标注行为动词（如“反思建议”、“准入校验”）；必须包含判定门禁（$\theta$ 阈值或成功/失败分支）与向上闭环回滚箭头（Feedback Loop），严禁纯文本无图堆叠。

> [!IMPORTANT]
> ## 🌐 Language & Communication Rule
>
> - **Response language**: match the user's input and source materials. Explicit user override (e.g., "请用英文回答") takes precedence.
> - **Template format**: `design_spec.md` MUST follow its original English template structure (section headings, field names) regardless of conversation language. Content values may be in the user's language.

> [!IMPORTANT]
> ## 🔌 Compatibility With Generic Coding Skills
>
> - `ppt-master` is a repository-specific workflow, not a general application scaffold
> - Do NOT create `.worktrees/`, `tests/`, branch workflows, or generic engineering structure by default
> - On conflict with a generic coding skill, follow this skill unless the user explicitly says otherwise

## Main Pipeline Scripts

| Script | Purpose |
|--------|---------|
| `${SKILL_DIR}/scripts/source_to_md/pdf_to_md.py` | PDF to Markdown |
| `${SKILL_DIR}/scripts/source_to_md/doc_to_md.py` | Documents to Markdown — native Python for DOCX/HTML/EPUB/IPYNB, pandoc fallback for legacy formats (.doc/.odt/.rtf/.tex/.rst/.org/.typ) |
| `${SKILL_DIR}/scripts/source_to_md/excel_to_md.py` | Excel workbooks to Markdown — supports .xlsx/.xlsm; legacy .xls should be resaved as .xlsx |
| `${SKILL_DIR}/scripts/source_to_md/ppt_to_md.py` | PowerPoint to Markdown |
| `${SKILL_DIR}/scripts/source_to_md/web_to_md.py` | Web page to Markdown (supports WeChat via `curl_cffi`) |
| `${SKILL_DIR}/scripts/project_manager.py` | Project init / validate / manage |
| `${SKILL_DIR}/scripts/analyze_images.py` | Image analysis |
| `${SKILL_DIR}/scripts/latex_render.py` | LaTeX formula rendering (manifest-driven PNG assets) |
| `${SKILL_DIR}/scripts/image_gen.py` | AI image generation (multi-provider) |
| `${SKILL_DIR}/scripts/svg_quality_checker.py` | SVG quality check |
| `${SKILL_DIR}/scripts/total_md_split.py` | Speaker notes splitting |
| `${SKILL_DIR}/scripts/finalize_svg.py` | SVG post-processing (unified entry) |
| `${SKILL_DIR}/scripts/fireworks_bridge.py` | Fireworks Tech Graph bridge (geometry checking, template rendering, EMF sync) |
| `${SKILL_DIR}/scripts/svg_to_pptx.py` | Export to PPTX |
| `${SKILL_DIR}/scripts/update_spec.py` | Propagate a `spec_lock.md` color / font_family change across all generated SVGs |

For complete tool documentation, see `${SKILL_DIR}/scripts/README.md`.

## Template Index

| Index | Path | Purpose |
|-------|------|---------|
| Layout templates | `${SKILL_DIR}/templates/layouts/layouts_index.json` | Query available page layout templates |
| Brand presets | `${SKILL_DIR}/templates/brands/brands_index.json` | Query available brand identity presets (color / typography / logo / voice) |
| Visualization templates | `${SKILL_DIR}/templates/charts/charts_index.json` | Query available visualization SVG templates (charts, infographics, diagrams, frameworks) |
| Icon library | `${SKILL_DIR}/templates/icons/` | See `${SKILL_DIR}/templates/icons/README.md`; search icons on demand with `ls templates/icons/<library>/ \| grep <keyword>` |

## Standalone Workflows

| Workflow | Path | Purpose |
|----------|------|---------|
| `topic-research` | `workflows/topic-research.md` | Pre-pipeline — gather web sources when the user supplies only a topic with no source files |
| `create-template` | `workflows/create-template.md` | Standalone layout template creation workflow |
| `create-brand` | `workflows/create-brand.md` | Standalone brand-only template creation (identity preset; no SVG page roster) |
| `resume-execute` | `workflows/resume-execute.md` | Phase B entry — resume execution in a fresh chat after Phase A (Step 1–5) completed in another session (split mode) |
| `verify-charts` | `workflows/verify-charts.md` | Chart coordinate calibration — run after SVG generation if the deck contains data charts |
| `customize-animations` | `workflows/customize-animations.md` | Object-level PPTX animation customization — run only when the user explicitly asks to tune animation order/effects/timing |
| `live-preview` | `workflows/live-preview.md` | Browser-based live preview — auto-started during generation and re-enterable any time the user mentions "live preview", "preview", "看效果", or wants to click/select a slide element |
| `visual-review` | `workflows/visual-review.md` | Detailed per-page visual review and atomic layout fixes — run when explicitly requested; Executor also performs the lightweight design checklist in Step 6 by default. |
| `academic-figure` | `workflows/academic-figure.md` | Standalone publication-grade academic architecture and pipeline figure creation (Figure 1, Methodology Overview; PaperBanana powered) |

---

## Workflow

### Step 1: Source Content Processing

🚧 **GATE**: User has provided source material (PDF / DOCX / EPUB / URL / Markdown file / text description / conversation content — any form is acceptable).

> **No source content?** When the user supplies only a topic name or requirements without any file or substantive description, run the [`topic-research`](workflows/topic-research.md) workflow first, then return here with its products as input.

When the user provides non-Markdown content, convert immediately:

| User Provides | Command |
|---------------|---------|
| PDF file | `python3 ${SKILL_DIR}/scripts/source_to_md/pdf_to_md.py <file>` |
| DOCX / Word / Office document | `python3 ${SKILL_DIR}/scripts/source_to_md/doc_to_md.py <file>` |
| XLSX / XLSM / Excel workbook | `python3 ${SKILL_DIR}/scripts/source_to_md/excel_to_md.py <file>` |
| CSV / TSV | Read directly as plain-text table source |
| PPTX / PowerPoint deck | `python3 ${SKILL_DIR}/scripts/source_to_md/ppt_to_md.py <file>` |
| EPUB / HTML / LaTeX / RST / other | `python3 ${SKILL_DIR}/scripts/source_to_md/doc_to_md.py <file>` |
| Web link | `python3 ${SKILL_DIR}/scripts/source_to_md/web_to_md.py <URL>` |
| WeChat / high-security site | `python3 ${SKILL_DIR}/scripts/source_to_md/web_to_md.py <URL>` (requires `curl_cffi`, included in `requirements.txt`) |
| Markdown | Read directly |

> **Office vector assets (EMF/WMF) from DOCX/PPTX sources**:
> `doc_to_md.py` / `ppt_to_md.py` extract embedded Office vector images (.emf/.wmf)
> alongside bitmap images. After `import-sources`, these land in `images/`
> together with `image_manifest.json` and are first-class assets in §VIII Image Resource List.
>
> **Do NOT convert EMF/WMF to PNG.** The PPT Master pipeline preserves them as external
> references (`finalize_svg.py` skips them) and `svg_to_pptx.py` embeds them as
> PPTX-native media via `image/x-emf` / `image/x-wmf` MIME — PowerPoint renders them at full vector fidelity.
> Converting via LibreOffice/Inkscape introduces CJK font substitution drift and
> rasterization loss; the original EMF/WMF is always higher fidelity than the converted PNG.
>
> Browser-based live preview cannot render EMF (will show blank) — this is expected;
> the PPTX output is the source of truth.

**✅ Checkpoint — Confirm source content is ready, proceed to Step 2.**

---

### Step 2: Project Initialization

🚧 **GATE**: Step 1 complete; source content is ready (Markdown file, user-provided text, or requirements described in conversation are all valid).

```bash
python3 ${SKILL_DIR}/scripts/project_manager.py init <project_name> --format <format>
```

Format options: `ppt169` (default), `ppt43`, `xhs`, `story`, etc. For the full format list, see `references/canvas-formats.md`.

Import source content (choose based on the situation):

| Situation | Action |
|-----------|--------|
| Has source files (PDF/MD/etc.) | `python3 ${SKILL_DIR}/scripts/project_manager.py import-sources <project_path> <source_files...> --move` |
| User provided text directly in conversation | No import needed — content is already in conversation context; subsequent steps can reference it directly |

> ⚠️ **MUST use `--move`** (not copy): all source files — Step 1's generated Markdown, original PDFs / MDs / images — go into `sources/` via `import-sources --move`. After execution they no longer exist at the original location. Intermediate artifacts (e.g., `_files/`) are handled automatically.

**✅ Checkpoint — Confirm project structure created successfully, `sources/` contains all source files, converted materials are ready. Proceed to Step 3.**

---

### Step 3: Template Option

🚧 **GATE**: Step 2 complete; project directory structure is ready.

**Default — 算法与流水线技术对比风格 (Algorithm Pipeline Brand) 作为科技风格默认模板。** 当用户未显式传入其他模板目录路径时，默认直接采用 `templates/brands/algorithm-pipeline/` 作为全套幻灯片的基础品牌与视觉规范（极净白底 `#FFFFFF`、双轨对比主色 `#0070C0` 科技蓝 / `#2E7D32` 工程绿、胶囊药丸标题、多阶段处理流、中间态特征图、逆变换对齐闭环、底部公式/对比表/注意事项三列分析）。

**Template flow triggers ONLY on explicit directory paths** supplied by the user in their initial message. The trigger rule is mechanical, not interpretive:

| User input contains | Step 3 action |
|---|---|
| One or more explicit template directory paths (each resolves to a directory containing `design_spec.md` with `kind: brand` / `kind: layout` / `kind: deck` in its YAML frontmatter) | Read each spec's `kind`, dispatch per the kind matrix below, fuse if multiple |
| Anything else — bare template names, style descriptions, vague intent, or silence | 默认应用 **算法与流水线技术对比风格 (Algorithm Pipeline Brand)** 规范推进 Step 4 |

There is no slug matching, no name lookup, no fuzzy resolution. A name without a path does not trigger — the user must give a path the AI can `cd` into.

> Style descriptions ("麦肯锡风格" / "Keynote 风" / "极简风" / etc.) never trigger Step 3. They flow into Strategist's Eight Confirmations as a style brief (color / typography / tone in confirmations e–g).

> Bare names ("academic_defense", "招商银行", "anthropic") do NOT trigger Step 3 even if a matching directory exists in the library. The user must give a path. AI must not "helpfully" resolve a name to a path.

> "What templates exist?" is out-of-band Q&A — answer by listing entries from `brands_index.json` / `layouts_index.json` / `decks_index.json` together with their paths. Listing alone does not advance the pipeline; the user must send a path back to trigger Step 3.

> To create a new layout or deck, read [`workflows/create-template.md`](workflows/create-template.md). To create a new brand, read [`workflows/create-brand.md`](workflows/create-brand.md).

#### Three template kinds

The architecture has three independent reference bundles. Full schema in [`docs/zh/templates-architecture.md`](../../docs/zh/templates-architecture.md). Summary:

| Kind | Physical dir | Contains | Frontmatter |
|---|---|---|---|
| **brand** | `templates/brands/<id>/` | identity-only segment: color / typography / logo / voice / icon style | `kind: brand` |
| **layout** | `templates/layouts/<id>/` | structure-only segment: canvas / page structure / page types / SVG roster | `kind: layout` |
| **deck** | `templates/decks/<id>/` | full replica: identity + structure + middle (template overview) segments | `kind: deck` |

**Segment ownership** (governs fusion override priority):

| Segment | Sections | Owner kind on fusion |
|---|---|---|
| Identity | Color Scheme / Typography / Logo / Voice & Tone / Icon Style | brand |
| Structure | Canvas / Page Structure / Page Types / SVG Roster | layout |
| Middle | Template Overview (use cases / design intent) | deck (no other kind writes this) |

#### Single-path dispatch

| User path's `kind` | Step 3 action |
|---|---|
| `kind: brand` | Copy `design_spec.md` + logo files + asset subdirs (`images/` / `illustrations/` / `icons/`) into `<project>/templates/`. Strategist locks identity segment as truth; structure stays free. |
| `kind: layout` | Copy `design_spec.md` + SVG roster + asset files into `<project>/templates/`. Strategist locks structure; identity decided in Eight Confirmations e–g. |
| `kind: deck` | Copy everything (`design_spec.md` + SVGs + logos + assets) into `<project>/templates/`. Strategist locks all segments; Eight Confirmations narrows to deck-content fields (audience / page count / outline / tone tweaks). |

```bash
TEMPLATE_DIR=<user-supplied path>
cp -r ${TEMPLATE_DIR}/* <project_path>/templates/
```

The single-line copy suffices for all three kinds — the spec's `kind` field tells Strategist how to read it; downstream code doesn't distinguish.

#### Multi-path fusion

When the user gives two or more paths of **different kinds**, Step 3 fuses them into a single `<project>/templates/design_spec.md`. **Default granularity is segment-level integer replacement** — entire identity / structure / middle segments are taken from the highest-priority source for that segment, no implicit field-level mixing.

Override priority by segment:

| Combination | Identity from | Structure from | Middle from |
|---|---|---|---|
| brand only | brand | (free design) | (none) |
| layout only | (free design) | layout | (none) |
| deck only | deck | deck | deck |
| brand + layout | brand | layout | (none) |
| brand + deck | brand (overrides deck) | deck | deck |
| layout + deck | deck | layout (overrides deck) | deck |
| brand + layout + deck | brand | layout | deck |

Field-level micro-adjustment (e.g. "use anthropic brand but primary changed to #FF0000") is **not** part of Step 3 fusion — it flows into Strategist Eight Confirmations e–g as a normal user request.

#### Same-kind multiple paths — conflict resolution

When the user gives two paths of the **same kind** (e.g. `brands/anthropic` + `brands/google`), Step 3 surfaces a conflict prompt before fusing — like resolving a git merge conflict:

```
AI: 你给了两个 brand，检测到段级冲突：
    - Color Scheme（Anthropic 橙红 vs Google 多色）
    - Typography（Styrene/AnthropicSans vs GoogleSans/Roboto）
    - Logo（Anthropic 标 vs Google 标）
    - Voice & Tone（restrained vs friendly）
    - Icon Style（stroke vs filled）

    要 (a) 全部按 Anthropic / (b) 全部按 Google / (c) 逐段挑？
```

Rules:
- Default: no implicit ordering — every cross-source segment difference is reported as a conflict
- Only when the user picks `(c)` does AI walk through each segment one by one
- Field-level conflicts are out of scope — segment-level only
- Three or more same-kind paths are not supported — ask the user to converge to at most two

#### Fused spec provenance

When fusion happens (any multi-path case), the resulting `<project>/templates/design_spec.md` carries a provenance block immediately under its H1:

```markdown
> **Fused from:**
> - deck: `templates/decks/招商银行/` （base）
> - brand: `templates/brands/anthropic/` （identity override）
> - layout: `templates/layouts/academic_defense/` （structure override）
> - conflicts resolved: Color Scheme from anthropic（user picked a）
```

Single-path Step 3 does **not** add provenance (the source is self-evident from the copied files).

**✅ Checkpoint — Default path proceeds to Step 4 without user interaction. If the user supplied one or more explicit template paths, those have been dispatched (or fused) into `<project_path>/templates/` before advancing.**

---

### Step 4: Strategist Phase (MANDATORY — cannot be skipped)

🚧 **GATE**: Step 3 complete; default free-design path taken, or (if triggered) template files copied into the project.

First, read the role definition:
```
Read references/strategist.md
```

> ⚠️ **Mandatory gate**: before writing `design_spec.md`, Strategist MUST `read_file templates/design_spec_reference.md` and follow its full I–XI section structure. See `strategist.md` Section 1.

**Eight Confirmations** (full template: `templates/design_spec_reference.md`):

⛔ **BLOCKING**: present the Eight Confirmations as a single bundled recommendation set and **wait for explicit user confirmation or modification** before outputting Design Specification & Content Outline. This is the single core confirmation point — once confirmed, all subsequent steps proceed automatically.

1. Canvas format
2. Page count range
3. Target audience
4. Style objective
5. Color scheme
6. Icon usage approach
7. Typography plan, including formula rendering policy
8. Image usage approach

**Content Logic & Sufficiency Gate (before presenting the Eight Confirmations)**: first shape the topic into an explanatory chain, then use that chain to recommend page count and outline. For problem-solving or system-introduction topics, use this three-step logic:

1. **问题是什么 (Problem)** — name the observed need, failure, constraint, or decision; make clear who is affected and why the audience should care.
2. **为何会出现 (Cause)** — explain the underlying mechanism, context, or evidence that produces the problem. Distinguish verified facts from assumptions; do not replace causality with a generic “current situation” paragraph.
3. **解决方案是什么 (Solution)** — show how the proposed system or action addresses the cause, including the relevant workflow, roles, inputs/outputs, quality gates, failure/recovery path, and expected result. Select the details that prove the solution; do not merely list feature names.

This is a reasoning scaffold, not a mandatory three-slide structure. For topics that are not problem-oriented, translate it into the equivalent chain **question/context → explanation/mechanism → answer/recommendation**. Before locking the page outline, make a compact content ledger of the audience's must-understand points and map each point to a page and a source/evidence anchor. For every planned page, the outline should state its takeaway and the facts or relationships that support it. Check that a reader can understand what the subject is, why it matters, and how the described approach works. If the chain cannot fit clearly in the requested page count, recommend adding pages or reorganizing the narrative before removing essential explanatory content; when page count is fixed, compress repetition and secondary detail first. Do not use abstract value claims, whitespace, decorative imagery, or speaker notes as substitutes for missing on-slide explanation, and do not invent details to satisfy the outline.

**Mandatory — split-mode note** (not a ninth confirmation): after listing the eight confirmation details, you MUST append exactly one short line (rendered in the user's language, prefixed with 💡) about generation mode. Pick the variant by qualitative read of Phase A signals — recommended page count, source-material bulk, whether `topic-research` ran with substantial web-fetch accumulation:

| Signal read | Line content |
|---|---|
| Heavy (long page count / bulky sources / heavy web-fetch accumulation) | State estimated page count and large source size; recommend switching to [split mode](workflows/resume-execute.md) after Step 5 — stop this chat, open a fresh window and input `继续生成 projects/<project_name>` to enter Phase B (SVG generation + export); no response or "continue" = default continuous mode. |
| Normal (default) | State scale is moderate, default continuous mode generates in one go; if mid-way window switch is desired, input `继续生成 projects/<project_name>` after Step 5 to switch to [split mode](workflows/resume-execute.md). |

This line is required output every run — the user must always see the mode choice exists. Whether to act on it is the user's call.

**Formula rendering policy lives inside item 7 (Typography plan)**:

| Policy | Behavior |
|---|---|
| `mixed` (default) | Strategist renders complex formula-worthy expressions as PNG assets; simple inline expressions remain editable text / Unicode |
| `render-all` | Strategist renders every formula-worthy expression as PNG assets |
| `text-only` | No formula rendering; formulas remain editable text / Unicode |

After the Eight Confirmations are approved and **before outputting `design_spec.md` / `spec_lock.md`**, if the confirmed formula policy is `mixed` or `render-all` and the content contains formula-worthy expressions, Strategist MUST:

1. Identify explicit LaTeX and any source expressions that should be faithfully structured as formulas.
2. Write `<project_path>/images/formula_manifest.json` with only the formulas selected for rendering.
3. Run:
   ```bash
   python3 ${SKILL_DIR}/scripts/latex_render.py <project_path>
   ```
4. Include the rendered formula PNGs as `Acquire Via: formula`, `Status: Rendered`, `Type: Latex Formula` rows in `design_spec.md §VIII Image Resource List`; also list them in `spec_lock.md images` with `| no-crop`.

The formula renderer uses a provider fallback chain by default: `codecogs,quicklatex,mathpad,wikimedia`. The first three are color-aware; Wikimedia is an availability fallback. Formula PNGs are transparent by default: manifest `background` is the temporary render matte and transparency-removal reference, not a retained final background unless `transparent: false` is set for that item. Do not scan `spec_lock.md` for `$...$` or `$$...$$`. Dollar-delimited math in source material is only a signal for Strategist; the renderer consumes the explicit manifest.

If the user provided images or formula PNGs were rendered, run analysis **before outputting the design spec**:
```bash
python3 ${SKILL_DIR}/scripts/analyze_images.py <project_path>/images
```

> ⚠️ **Image handling**: NEVER directly read / open / view image files (`.jpg`, `.png`, etc.). All image info comes from `analyze_images.py` output or the Design Spec's Image Resource List.

**Output**:
- `<project_path>/design_spec.md` — human-readable design narrative
- `<project_path>/spec_lock.md` — machine-readable execution contract (skeleton: `templates/spec_lock_reference.md`); Executor re-reads before every page

**✅ Checkpoint — Phase deliverables complete, auto-proceed to next step**:
```markdown
## ✅ Strategist Phase Complete
- [x] Eight Confirmations completed (user confirmed)
- [x] Split-mode note appended below the eight items (heavy or normal variant)
- [x] Design Specification & Content Outline generated
- [x] Execution lock (spec_lock.md) generated
- [ ] **Next**: Auto-proceed to [Image_Generator / Executor] phase
```

---

### Step 5: Image Acquisition Phase (Conditional)

🚧 **GATE**: Step 4 complete; Design Specification & Content Outline generated and user confirmed. Any formula rows already have `Acquire Via: formula` and `Status: Rendered`.

> **Visual-Expression Rule (Mandatory)**: For each planned page, select a visual expression that matches its content. Dense text may be edited down, organized with typographic hierarchy, or split across pages; use a diagram or image only when it communicates the content more clearly. Do not inject AI image rows solely because a page contains text, a table, or code. See `references/premium-visual-language.md` and `references/shared-standards.md` §9.

> **Trigger**: At least one row in the resource list has `Acquire Via: ai` and/or `Acquire Via: web`. If every row is `user`, `formula`, or `placeholder`, skip to Step 6.

**Always load the common framework**:

```
Read references/image-base.md
```

Then **lazy-load the path-specific reference** for each row that actually needs it:

| Acquire Via | Load reference (only if any such row exists) | Run |
|---|---|---|
| `ai` | `references/image-generator.md` | `python3 ${SKILL_DIR}/scripts/image_gen.py --manifest <project_path>/images/image_prompts.json` |
| `web` | `references/image-searcher.md` | `python3 ${SKILL_DIR}/scripts/image_search.py ...` |
| `user` / `placeholder` | (skip) | (skip) |

A deck with only `ai` rows never loads `image-searcher.md`; a deck with only `web` rows never loads `image-generator.md`. A mixed deck loads both, processes each row through its own path, and writes both `image_prompts.json` and `image_sources.json`.

> ⚠️ **In-pipeline ai path MUST use manifest mode** — even when only 1 ai row exists. Write `images/image_prompts.json` first, then run `image_gen.py --manifest`, then `image_gen.py --render-md` to produce the `image_prompts.md` sidecar. The positional form (`image_gen.py "prompt" ...`) is reserved for **out-of-pipeline one-off testing / single-image fixups** — it skips manifest + sidecar, leaving no audit trail.

Workflow:

1. Extract all rows with `Status: Pending` and `Acquire Via ∈ {ai, web}` from the design spec
2. Generate prompts (ai rows) and/or run search (web rows) per [image-base.md](references/image-base.md) §2 dispatch table
3. Verify every row reaches a terminal status: `Generated` (ai success), `Sourced` (web success), or `Needs-Manual`

**✅ Checkpoint — Confirm acquisition attempted for every row**:
```markdown
## ✅ Image Acquisition Phase Complete
- [x] image_prompts.json created (when any ai rows processed)
- [x] image_prompts.md sidecar rendered (when any ai rows processed)
- [x] image_sources.json created (when any web rows processed)
- [x] Each row: status is `Generated` / `Sourced` / `Needs-Manual` (no `Pending` remaining)
```

**Default — auto-proceed to Step 6.** Only when the user's Step 4 response explicitly opted into split mode (in reply to the optional hint), output the Phase A hand-off below and stop this conversation:

  ```markdown
  ## ✅ Phase A Complete
  - [x] Spec: `design_spec.md`, `spec_lock.md`
  - [x] Resources: `sources/`, `images/`, `templates/`
  - [ ] **Next**: open a fresh chat window and input `继续生成 projects/<project_name>` to enter Phase B via the [`resume-execute`](workflows/resume-execute.md) workflow.
  ```

> On acquisition failure, do NOT halt — follow the Failure Handling rule in [image-base.md](references/image-base.md) §5: retry once, then mark the row `Needs-Manual`, report to user, and continue to the checkpoint above.

---

### Step 6: Executor Phase

🚧 **GATE**: Step 4 (and Step 5 if triggered) complete; all prerequisite deliverables are ready.

Read the role definition based on the selected style:
```
Read references/executor-base.md          # REQUIRED: common guidelines
Read references/shared-standards.md       # REQUIRED: SVG/PPT technical constraints
Read references/premium-visual-language.md # REQUIRED: diagram, table, and color grammar
Read references/executor-general.md       # General flexible style
Read references/executor-consultant.md    # Consulting style
Read references/executor-consultant-top.md # Top consulting style (MBB level)
```

> Only read executor-base + shared-standards + one style file.

**Design Parameter Confirmation (Mandatory)**: before the first SVG, output key design parameters from the spec (canvas dimensions, color scheme, font plan, body font size). See executor-base.md §2.

**Live Preview Auto-Startup (Mandatory)**: before the first SVG, automatically start the browser editor in live mode and keep it running continuously through Executor + Step 7 export:
```bash
python3 ${SKILL_DIR}/scripts/svg_editor/server.py <project_path> --live
```
- Start it immediately when Executor begins; `svg_output/` may be empty. Editor opens at `http://localhost:5050`; port conflict → `--port <other>` and report the actual URL.
- Run it as a long-running side process/session; do not wait for it to exit before generating SVG pages. Do not wait for user confirmation after startup.
- **Service must keep running** until one of: (a) the user clicks **Exit preview** in the browser, or (b) the user explicitly asks in chat to stop it. Generation continues even if the user closes the editor.
- **Do NOT read or apply submitted annotations during generation.** Users may annotate at any time, but Executor proceeds without touching them. The window to apply annotations opens only after Step 7 completes — see [`workflows/live-preview.md`](workflows/live-preview.md).
- UI button semantics and editor details: see [`workflows/live-preview.md`](workflows/live-preview.md) Notes.

**Pre-generation Batch Read (Mandatory)**: before the first SVG, batch-read every distinct layout SVG referenced in `spec_lock.page_layouts` and every distinct chart SVG referenced in `spec_lock.page_charts` (plus any §VII backup charts). One read per file, up front — do not re-read these during page generation. See executor-base.md §1.0.

**Per-page spec_lock re-read (Mandatory)**: before **each** SVG page, `read_file <project_path>/spec_lock.md` and use only its colors / fonts / icons / images, plus the per-page `page_rhythm` / `page_layouts` / `page_charts` lookups (resolves to template SVGs already loaded in the batch read above). Resists context-compression drift on long decks. See executor-base.md §2.1.

> ⚠️ **Main-agent only**: SVG generation MUST stay in the current main agent — page design depends on full upstream context. Do NOT delegate to sub-agents.
> ⚠️ **Generation rhythm**: generate pages sequentially, one at a time, in the same continuous context. Do NOT batch (e.g., 5 per group).

**Visual Construction Phase**: generate SVG pages sequentially, one at a time, in one continuous pass → `<project_path>/svg_output/`
- **Text Anti-Overlap, Container Boundary & Code Block Safe Margin (严禁字体重叠与边框容器溢出)**: SVG text does NOT auto-wrap. 任何卡片、步骤条、代码块、状态框内的单行代码与文字，必须严格受限于其所在的容器 `<rect>` 边界，且保留 $\ge 15\text{px}$ 安全呼吸边距。代码框内等宽半角文本单行严禁超过 36 字符（长 JSON 或多赋值语句必须按键值对拆为多行）。单行普通文本在 3 栏卡片内严禁超过 22 个中文字符，2 栏卡片内严禁超过 34 个中文字符，垂直行高 $\Delta y \ge \text{font\_size} \times 1.35$。
- **Pill Badges & Flowchart Line Shielding (胶囊徽章与流程图防压字硬约束)**: Badge width must strictly bound inner text ($\text{width} \ge \text{text\_length} \times \text{char\_width} + \text{icon\_width} + 20\text{px} + \text{char\_count} \times \text{letter\_spacing}$). Flowchart/state machine lines must never cut through unshielded text; always place protective solid background rects under text labels sitting on paths (see `references/shared-standards.md` §4.3 and §4.4).
- **Connector Routing & Zero Container Intrusion (严禁连线与箭头侵入其他卡片框)**: 跨板块、跨步骤的折线、连线与附属标牌，必须严格走外侧走廊或净空隙安全绕行，严禁切穿、横扫或覆盖非关联卡片的内部及边框（见 `references/shared-standards.md` §4.4）。
- **Post-Generation Container Overflow & Line Intrusion Auto-Gate (生成后容器边框溢出与连线侵入自动拦截门禁)**: `svg_quality_checker.py` 强制对所有卡片/代码块/状态框的 `<rect>` 与其内 `<text>` 进行包围盒边界碰撞扫描，同时对所有跨卡片 `<path>`/`<line>` 及说明标牌进行穿透侵入检测，任何文字溢出边框或连线侵入其他框将直接抛出 ERROR 并阻断导出。

**Quality Check Gate (Mandatory)** — after all SVGs, BEFORE annotation handling and speaker notes:
```bash
python3 ${SKILL_DIR}/scripts/svg_quality_checker.py <project_path>
```
- Any `error` (banned SVG features, `<clipPath>` defined outside `<defs>`, unescaped bare `&` / `<` / `>`, viewBox mismatch, text overlap / card boundary overflow, spec_lock drift, etc.) MUST be fixed before proceeding — return to Visual Construction, regenerate that page, re-run check.
- `warning` entries (low-res image, non-PPT-safe font tail, long text lines, etc.): fix when straightforward, otherwise acknowledge and release.
- Run against `svg_output/` (not after `finalize_svg.py` — finalize rewrites SVG and masks violations).


**Logic Construction Phase**: generate speaker notes → `<project_path>/notes/total.md`

**✅ Checkpoint — Confirm all SVGs and notes are fully generated and quality-checked. Proceed directly to Step 7 post-processing**:
```markdown
## ✅ Executor Phase Complete
- [x] Live preview started and kept available at the reported URL
- [x] All SVGs generated to svg_output/
- [x] svg_quality_checker.py passed (0 errors)
- [x] Speaker notes generated at notes/total.md
```

> **Chart pages?** If this deck contains data charts (bar / line / pie / radar / etc.), run the standalone [`verify-charts`](workflows/verify-charts.md) workflow before Step 7 to calibrate coordinates. AI models routinely introduce 10–50 px errors when mapping data to pixel positions; verify-charts eliminates that class of error. Skip if no chart pages.

> **Visual and content self-check (Mandatory)**: after `svg_quality_checker.py` passes and before speaker notes, review each page against `references/premium-visual-language.md` §5 and the Step 4 Content Logic & Sufficiency Gate. In addition to visual hierarchy, content-fit, spacing/alignment, color restraint, diagram/table legibility, and consistency with neighboring pages, verify that the page communicates its promised takeaway with enough concrete, source-backed detail; for a problem-solving deck, confirm the problem → cause → solution chain remains understandable across the deck. A clean layout is not evidence of sufficient content. Fix either design defects or missing explanatory links in the SVG and rerun the quality checker. This lightweight pass is part of normal execution. The standalone [`visual-review`](workflows/visual-review.md) remains available when the user asks for a deeper rendered-image review.

---

### Step 7: Post-processing & Export

🚧 **GATE**: Step 6 complete; all SVGs generated to `svg_output/`; speaker notes `notes/total.md` generated.

🚧 **Image readiness GATE** (when Step 5 left ai rows in `Needs-Manual`): every expected file must exist at `project/images/<filename>` before running 7.1.

> If files are missing: PAUSE, list the missing filenames, point the user to `images/image_prompts.md` (each `### Image N:` block is paste-ready for ChatGPT / Gemini / Midjourney; auto-generated from `image_prompts.json`) and the required placement `project/images/<filename>`. Resume Step 7.1 only after all expected files are in place. `finalize_svg.py` and `svg_to_pptx.py` do not detect missing files at this layer — proceeding with gaps produces a deck with broken image references.

> ⚠️ Run the three sub-steps **one at a time** — each must complete successfully before the next.
> ❌ **NEVER** combine them into a single code block or shell invocation.

Canonical three-command pipeline (mirrors `references/shared-standards.md` §5):

**Step 7.1** — Split speaker notes:
```bash
python3 ${SKILL_DIR}/scripts/total_md_split.py <project_path>
```

**Step 7.2** — SVG post-processing (icon embedding / image crop & embed / text flattening / rounded rect to path):
```bash
python3 ${SKILL_DIR}/scripts/finalize_svg.py <project_path>
```

**Step 7.3** — Export PPTX (embeds speaker notes by default):
```bash
# Create PPT directory if not exists, then export with explicit output path (仅保留最新一份):
mkdir -p <project_path>/PPT/
python3 ${SKILL_DIR}/scripts/svg_to_pptx.py <project_path> -o <project_path>/PPT/<project_name>.pptx
```

> ⚠️ **GLOBAL CONSTRAINT (Rule 10 - 同一PPT仅保留最新一份):** The `-o` flag with explicit `<project_path>/PPT/<project_name>.pptx` output path is **MANDATORY**. Do NOT omit `-o` or use the default `exports/` directory. All generated `.pptx` files MUST be saved within the project's `PPT/` subdirectory to ensure project artifacts are self-contained. **严禁在同一项目下堆积带有不同时间戳的多个历史陈旧 `.pptx`**。重新导出或二次生成时，必须直接覆盖或清理该项目旧版本的 `.pptx`，确保 `<project_path>/PPT/` 目录下始终仅有且仅保留最新一份最终交付物。

> A copy of `svg_output/` is still snapshotted to `backup/<timestamp>/svg_output/` for re-export capability.


> The native pptx consumes `svg_output/` directly so the converter can preserve
> high-fidelity primitives (icon `<use>` placeholders, image `preserveAspectRatio`
> → `srcRect`, rounded rect `rx/ry` → `prstGeom roundRect`). The `svg_output/`
> snapshot in `backup/<timestamp>/` is always written so the project can be
> re-exported from frozen SVG sources without re-running the LLM. The SVG-rendered
> preview pptx is opt-in via `--svg-snapshot` — live preview already provides the
> SVG visual reference, so it's only needed when you want a self-contained file
> to share. Pass `-s output` or `-s final` to force a single source if you need it.

> **Paragraph editability vs line fidelity** — by default every dy-stacked line is
> its own PowerPoint text frame, preserving exact SVG layout. Add `--merge-paragraphs`
> only when the user explicitly asks for an editable / wrap-friendly export (e.g.
> "I want to edit the abstract as one block", "make text boxes resizable / reflow"):
> mergeable paragraph blocks collapse into one editable text frame with multiple
> `<a:p>`, at the cost of PowerPoint re-wrapping inside each box. Default off keeps
> pixel-fidelity; turn it on per the user's request, not on your own judgement.

**Optional animation flags** (the defaults already enable rich entrance animations — adjust only when the user asks for something different):
- `-t <effect>` — page transition. Default `fade`. Options: `fade` / `push` / `wipe` / `split` / `strips` / `cover` / `random` / `none`.
- `-a <effect>` — per-element entrance animation. Default `auto` (map effect from group id: chart→wipe, card-/step-/pillar-→fly, title/takeaway→fade; image-like ids `hero` / `figure-` / `image` / `img-` / `kpi` cycle a richer pool — zoom / dissolve / circle / box / diamond / wheel — so multiple images vary across the deck). Pass `none` to disable, a specific effect like `fade`, or `mixed` for the legacy 16-effect cycle. Requires top-level `<g id="...">` groups (already required by Executor).
- `--animation-trigger {on-click,with-previous,after-previous}` — Start mode (matches PowerPoint's animation-pane Start dropdown). Default `after-previous` (click-free cascade; pace via `--animation-stagger`). Use `on-click` for presenter-paced reveals, or `with-previous` for all-at-once.
- `--animation-config <path>` — optional object-level sidecar. Default: `<project_path>/animations.json` when present.
- `--auto-advance <seconds>` — kiosk-style auto-play.

**Optional custom animations** (only when the user asks to tune animation order/effects/timing for specific objects):

Run the standalone [`customize-animations`](workflows/customize-animations.md) workflow. Default export already has global entrance animation; do not create `animations.json` unless object-level customization was requested.

**Optional recorded narration** (only when the user asks for narrated/video export):

Run the standalone [`generate-audio`](workflows/generate-audio.md) workflow. The AI picks a narration backend (`edge` by default, or a configured cloud provider such as ElevenLabs / MiniMax / Qwen / CosyVoice for high-quality or cloned voices), asks the user once (backend + voice + rate/settings + embed-or-not, all with recommended values), then executes `notes_to_audio.py` and (if chosen) re-exports the PPTX with `--recorded-narration audio`.

Do NOT call `notes_to_audio.py` directly without going through the workflow — `--voice` / `--voice-id` is required and the workflow produces the locale/provider-aware recommendation that makes the choice meaningful.

Full effect list, anchor logic, and limits: [`references/animations.md`](references/animations.md).

> ❌ **NEVER** substitute `cp` for `finalize_svg.py` — finalize performs multiple critical processing steps
> ❌ **NEVER** force `-s output` for the legacy/preview pptx (PowerPoint's internal SVG parser drops icons and rounded corners). The default auto-split already gives native the high-fidelity source it needs without touching legacy.
> ❌ **NEVER** use `--only` (it suppresses one of the two output files)

> **Post-export annotation window**: the preview service from Step 6 typically remains running after export. If the user submitted annotations in the browser (during Executor or after export) and now asks to apply them — they may quote the browser prompt (`Annotations saved. ... apply my annotations`), say "apply my annotations" / "应用注解" / equivalent — run [`live-preview`](workflows/live-preview.md) Step 2 to apply and re-export. Annotations submitted during generation are also handled here, not earlier.

> **Preview not running?** Any time the user mentions "live preview", "preview", "看效果", or wants to select/click a slide element and the service is not running, run [`live-preview`](workflows/live-preview.md) Step 1 to start it. If the service is already running, just point them at the URL — do not restart.

---

## Role Switching Protocol

Before switching roles, **MUST first read** the corresponding reference file. Output marker:

```markdown
## [Role Switch: <Role Name>]
📖 Reading role definition: references/<filename>.md
📋 Current task: <brief description>
```

---

## Reference Resources

| Resource | Path |
|----------|------|
| Shared technical constraints | `references/shared-standards.md` |
| Canvas format specification | `references/canvas-formats.md` |
| Image-text layout patterns (Primary structures + Modifier layers — combine freely) | `references/image-layout-patterns.md` |
| Image layout sizing (math for side-by-side container dimensions) | `references/image-layout-spec.md` |
| SVG image embedding | `references/svg-image-embedding.md` |
| Icon library | `templates/icons/README.md` |

---

## Notes

- Local preview: `python3 -m http.server -d <project_path>/svg_final 8000`
- **Troubleshooting**: on generation issues (layout overflow, export errors, blank images, etc.), check `docs/faq.md` for known solutions
