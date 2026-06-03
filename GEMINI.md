# Project Instructions

## Global PPT Generation Constraint

When generating a PPT for a project, you MUST modify the output directory to be within the **target** project's directory.

1.  **Identify Target Project Path**: Determine the directory of the project being documented (e.g., `/data/code/NonfunAgent` or `projects/my-deck`).
2.  **Create PPT Directory**: Ensure a `PPT/` subdirectory exists within that target project path. Use `mkdir -p` via shell command if necessary.
3.  **Specify Output Path**: When running the export script (`skills/ppt-master/scripts/svg_to_pptx.py`), use the `-o` or `--output` flag to save the generated `.pptx` file into the target project's `PPT/` directory.
4.  **Filename Convention**: Use the format `<project_name>_<timestamp>.pptx`.

**Example:**
For target project `/data/code/NonfunAgent`:
```bash
python3 skills/ppt-master/scripts/svg_to_pptx.py projects/NonfunAgent_Daily_Progress -o /data/code/NonfunAgent/PPT/NonfunAgent_Daily_Progress_20260527.pptx
```

This constraint takes precedence over the default `exports/` directory mentioned in `SKILL.md` or other documentation.

