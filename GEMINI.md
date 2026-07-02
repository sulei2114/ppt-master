# Project Instructions

## Global PPT Generation Constraint

1.  **Output Directory**: When generating a PPT for a project, you MUST modify the output directory to be within the **target** project's directory.
    *   Identify Target Project Path: Determine the directory of the project being documented (e.g., `/data/code/NonfunAgent` or `projects/my-deck`).
    *   Create PPT Directory: Ensure a `PPT/` subdirectory exists within that target project path. Use `mkdir -p` via shell command if necessary.
    *   Specify Output Path: When running the export script (`skills/ppt-master/scripts/svg_to_pptx.py`), use the `-o` or `--output` flag to save the generated `.pptx` file into the target project's `PPT/` directory.
    *   Filename Convention: Use the format `<project_name>_<timestamp>.pptx`.

2.  **Visual Style**: All PPTs generated MUST default to a **Minimalist White** style unless explicitly requested otherwise.
    *   Background: Pure white or very light gray.
    *   Typography: High legibility sans-serif fonts (e.g., Noto Sans SC).
    *   Accents: Professional blue or brand-specific colors used sparingly for emphasis.
    *   Layout: Ample whitespace, clean margins, and structured grids.

3.  **AI Agent / 机器人主题图标规范**：当幻灯片主题涉及 AI Agent、智能体、机器人、人工智能、算法或智能芯片时，在生成页面 SVG 代码时，必须优先在节点修饰、标题点缀、逻辑架构图等位置内联或调用 [ai-agent](file:///su_data/code/ppt-master/skills/ppt-master/templates/icons/ai-agent/) 目录下的蓝白科技矢量图标：
    *   智能体网络图标：[ai-agent-network.svg](file:///su_data/code/ppt-master/skills/ppt-master/templates/icons/ai-agent/ai-agent-network.svg)
    *   机器人面部图标：[ai-robot-face.svg](file:///su_data/code/ppt-master/skills/ppt-master/templates/icons/ai-agent/ai-robot-face.svg)
    *   智能芯片图标：[ai-chip.svg](file:///su_data/code/ppt-master/skills/ppt-master/templates/icons/ai-agent/ai-chip.svg)
    *   **色调一致性约束**：在页面中嵌入或内联上述图标时，**图标的所有色值（包括描边 `stroke`、填充 `fill` 等）必须与当前 PPT 方案确定的主题色系（如定义在 `spec_lock.md` 中的 `brand_color` 等）完全保持一致**。AI 在编写幻灯片 SVG 代码时，必须将图标模板中的默认硬编码色值动态替换为当前 PPT 的主色、辅助色或强调色，严禁使用与 PPT 整体配色方案冲突的硬编码色值。
    *   **在线自动生成与兜底机制**：如果需要的特定 AI/机器人主题图标在 [ai-agent](file:///su_data/code/ppt-master/skills/ppt-master/templates/icons/ai-agent/) 目录下不存在，**AI 助手在编写幻灯片 SVG 代码时必须根据上下文含义，当场在线手写编写出符合规范的全新 SVG 矢量代码节点**。新生成的 SVG 图标应符合规范（如 viewBox="0 0 24 24"，极简科技线条风格），确保与整体幻灯片的配色和设计风格融为一体，严禁因为缺乏对应的图标文件而缺失素材或报错。


**Example:**
For target project `/data/code/NonfunAgent`:
```bash
python3 skills/ppt-master/scripts/svg_to_pptx.py projects/NonfunAgent_Daily_Progress -o /data/code/NonfunAgent/PPT/NonfunAgent_Daily_Progress_20260527.pptx
```


