# 机器人监控系统 - Design Spec

> Human-readable design narrative — rationale, audience, style, color choices, content outline. Read once by downstream roles for context.
>
> Machine-readable execution contract: `spec_lock.md` (color / typography / icon / image short form). Executor re-reads `spec_lock.md` before every SVG page to resist context-compression drift. Keep both in sync; on divergence, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 机器人监控系统 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 3 |
| **Design Style** | General Consulting + tech professional |
| **Target Audience** | 毕业答辩评委、技术评审专家 |
| **Use Case** | 毕业设计答辩、项目技术汇报 |
| **Created Date** | 2026-06-03 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | Left/Right 60px, Top/Bottom 50px |
| **Content Area** | 1160×620 |

---

## III. Visual Theme

### Theme Style

- **Style**: tech professional
- **Theme**: Light theme
- **Tone**: professional, modern, technical

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | Page background |
| **Secondary bg** | `#F0F4F8` | Card background, section background |
| **Primary** | `#0D2137` | Deep blue - title decorations, key sections, icons |
| **Accent** | `#1E88E5` | Data highlights, key information |
| **Secondary accent** | `#FF9800` | Warning/anomaly markers |
| **Body text** | `#1A1A1A` | Main body text |
| **Secondary text** | `#616161` | Captions, annotations |
| **Tertiary text** | `#9E9E9E` | Supplementary info, footers |
| **Border/divider** | `#E0E0E0` | Card borders, divider lines |
| **Success** | `#4CAF50` | Positive indicators (normal status) |
| **Warning** | `#F44336` | Issue markers (fault status) |

### Gradient Scheme

```xml
<!-- Title accent gradient -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#0D2137"/>
  <stop offset="100%" stop-color="#1E88E5"/>
</linearGradient>

<!-- Background decorative gradient -->
<radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
  <stop offset="0%" stop-color="#1E88E5" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#1E88E5" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: modern CJK sans

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"`, `"PingFang SC"` | Arial | sans-serif |
| **Body** | `"Microsoft YaHei"`, `"PingFang SC"` | Arial | sans-serif |
| **Emphasis** | — | Georgia | serif |
| **Code** | — | Consolas, "Courier New" | monospace |

**Per-role font stacks**:

- Title: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: same as Body
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body font size = 18px

| Purpose | Ratio to body | Value | Weight |
| ------- | ------------- | ----- | ------ |
| Cover title | 2.5-5x | 60-72px | Bold |
| Page title | 1.5-2x | 28-32px | Bold |
| Subtitle | 1.2-1.5x | 22-26px | SemiBold |
| **Body content** | **1x** | **18px** | Regular |
| Annotation / caption | 0.7-0.85x | 13-15px | Regular |
| Page number | 0.5-0.65x | 10-12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: Height 80-100px, contains page title
- **Content area**: Height 520-560px, main content
- **Footer area**: Height 40px, page number

### Layout Pattern Library

| Pattern | Suitable Scenarios |
| ------- | ----------------- |
| **Single column centered** | Covers, conclusions, key points |
| **Three/four column cards** | Feature lists, parallel points |
| **Top-bottom split** | Processes, architectures |
| **Z-pattern** | Storytelling, sequential flow |

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Safe margin | 60px |
| Content block gap | 32px |
| Card gap | 24px |
| Card padding | 24px |
| Card border radius | 12px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/`
- **Usage method**: SVG placeholder `<use data-icon="library/icon-name" .../>`

### Icon Configuration

- **Library**: `tabler-outline`
- **Stroke width**: `2`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| Robot/Device | `tabler-outline/robot` | P01, P02 |
| Server | `tabler-outline/server` | P02 |
| Desktop/Web | `tabler-outline/device-desktop` | P02 |
| Database | `tabler-outline/database` | P02 |
| Eye/Monitor | `tabler-outline/eye` | P03 |
| Alert/Warning | `tabler-outline/alert-triangle` | P03 |
| Bug/Troubleshoot | `tabler-outline/bug` | P03 |
| Chart/Analysis | `tabler-outline/chart-line` | P03 |
| Check/Success | `tabler-outline/circle-check` | P02, P03 |
| Arrow down | `tabler-outline/arrow-down` | P02 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------ | ----- |
| P02 | layered_architecture | `templates/charts/layered_architecture.svg` | "Pick for 3-4 horizontal architecture layers (presentation/service/data), 2-4 module cards per layer, each card = title + 1-line description (description required, even if source brief). Skip if no per-module descriptions (use icon_grid) or no horizontal layering (use module_composition)." | Three-layer architecture diagram |
| P03 | vertical_pillars | `templates/charts/vertical_pillars.svg` | "Pick for 1×3 / 1×4 / 1×5 vertical column layout where each pillar = one independent category with title + bullets — PEST (Political/Economic/Social/Technological), four-pillar strategy overview, side-by-side independent categories. Skip for 2×2 quadrant (use quadrant_text_bullets), pricing tiers (use comparison_columns), or 2×2 parallel aspects (use labeled_card)." | Key functions overview |

**Runners-up considered**:

- `icon_grid` | rejected for P02: architecture needs clear layer separation, not flat icon grid
- `module_composition` | rejected for P02: no parent container wrapping child modules in this content
- `hub_spoke` | rejected for P02: three-layer architecture is sequential, not hub-centered

---

## VIII. Image Resource List

No images required for this project. All visuals will be created using SVG-native shapes, icons, and text.

---

## IX. Content Outline

### Part 1: 系统概述

#### Slide 01 - Cover

- **Layout**: Single column centered
- **Title**: 机器人监控系统
- **Subtitle**: 基于三层架构的机器人实时监控与故障排查平台
- **Info**: 毕业设计答辩 · 2026

#### Slide 02 - 系统总体架构

- **Layout**: Top-down layered architecture
- **Title**: 系统总体架构（三层架构）
- **Visualization**: layered_architecture
- **Content**:

  **1. 底层采集层（机器人端）**
  - 对接机器人控制柜（ABB、安川、国产六轴机器人）
  - 采集内容：单次任务启停状态、各关节电流/温度、伺服报警码、任务执行进度
  - 4G/以太网DTU模块，实时上传云端服务器

  **2. 中间服务层（后端核心）**
  - Java后端 + MySQL数据库，实时存入机器人数据、任务记录、故障日志
  - 配置异常阈值规则：关节电流超上限、温度超标、急停触发，自动标记异常
  - 缓存每次机器人完整任务全流程数据，用于故障排查溯源

  **3. 上层应用层（Web监控平台）**
  - PC网页端 + 手机移动端H5双界面（B/S架构）
  - 实时任务监控模块、异常告警模块、故障排查溯源模块

#### Slide 03 - 平台关键功能详解

- **Layout**: Three vertical pillars
- **Title**: 平台关键功能详解
- **Visualization**: vertical_pillars
- **Content**:

  **实时状态查看功能**
  - 机器人总览看板、单机器人详情页、任务运行日志
  - 2秒轮询刷新，实时同步机器人现场运行状态
  - 自动记录每次任务的开始时间、结束时间、运行结果

  **异常告警模块**
  - 机器人触发故障 → 后端识别异常 → Web页面弹窗红色告警
  - 同步推送短信/APP消息
  - 告警附带故障代码、发生时间、对应任务编号

  **故障排查溯源功能（重点创新点）**
  - 在线初步诊断：内置故障码数据库，自动匹配故障原因
  - 历史数据复盘：调取故障前5分钟实时参数曲线，对比正常工况
  - 故障分类统计：按月统计故障频次，汇总高频故障，辅助预防性维护

---

## X. Speaker Notes Requirements

- **Filename**: match SVG names (e.g., `01_cover.md`)
- **Content**: script key points, timing cues
- **Presentation purpose**: inform
- **Notes style**: formal

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`
7. Text characters: write typography & symbols as raw Unicode; XML reserved chars must be escaped as `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN (group opacity); set on each child element individually
- Image transparency uses overlay mask layer
- Inline styles only; external CSS and `@font-face` FORBIDDEN
