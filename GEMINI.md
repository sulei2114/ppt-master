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

**Example:**
For target project `/data/code/NonfunAgent`:
```bash
python3 skills/ppt-master/scripts/svg_to_pptx.py projects/NonfunAgent_Daily_Progress -o /data/code/NonfunAgent/PPT/NonfunAgent_Daily_Progress_20260527.pptx
```


