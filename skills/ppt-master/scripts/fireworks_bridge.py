#!/usr/bin/env python3
"""
Fireworks Tech Graph Bridge for PPT Master

Integrates fireworks-tech-graph geometry validation, template rendering, and 
SVG-to-EMF synchronization directly into the PPT Master pipeline.

Usage:
    python3 scripts/fireworks_bridge.py check <svg_file>
    python3 scripts/fireworks_bridge.py render <template_type> <output_svg> <json_spec>
    python3 scripts/fireworks_bridge.py export-emf <svg_file> [output_emf]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

SCRIPT_DIR = Path(__file__).resolve().parent
PPT_MASTER_ROOT = SCRIPT_DIR.parent

# Candidate locations for fireworks-tech-graph
FIREWORKS_SEARCH_PATHS = [
    Path("/su_data/code/RobocloudBrain/anomaly_monitor/skills/fireworks-tech-graph"),
    Path("/su_data/code/anomaly_monitor/skills/fireworks-tech-graph"),
    Path.home() / ".gemini/skills/drawio",
    Path.home() / ".gemini/skills/fireworks-tech-graph",
]


def find_fireworks_root() -> Optional[Path]:
    """Locate fireworks-tech-graph or drawio directory with scripts/fireworks.py."""
    for path in FIREWORKS_SEARCH_PATHS:
        if (path / "scripts" / "fireworks.py").is_file():
            return path
    return None


def run_fireworks_check(svg_path: Path) -> Dict[str, Any]:
    """Execute fireworks check to validate geometry, markers, composition, and XML."""
    fireworks_root = find_fireworks_root()
    if not fireworks_root:
        return {
            "ok": False,
            "error": "fireworks-tech-graph not found in candidate paths",
        }

    cmd = [
        sys.executable,
        str(fireworks_root / "scripts" / "fireworks.py"),
        "check",
        str(svg_path),
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.stdout.strip():
            try:
                return json.loads(proc.stdout)
            except json.JSONDecodeError:
                return {"ok": proc.returncode == 0, "raw_output": proc.stdout}
        return {"ok": proc.returncode == 0, "stderr": proc.stderr}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def render_from_template(template_name: str, output_path: Path, spec_json: str) -> bool:
    """Render a diagram SVG from built-in fireworks templates (architecture, agent-architecture, etc.)."""
    fireworks_root = find_fireworks_root()
    if not fireworks_root:
        print("Error: fireworks-tech-graph not found", file=sys.stderr)
        return False

    gen_script = fireworks_root / "scripts" / "generate-from-template.py"
    if not gen_script.is_file():
        print(f"Error: generator script missing at {gen_script}", file=sys.stderr)
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        str(gen_script),
        template_name,
        str(output_path),
        spec_json,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"Template rendering failed:\n{proc.stderr}", file=sys.stderr)
        return False
    return True


def export_emf(svg_path: Path, output_emf: Optional[Path] = None) -> bool:
    """
    Ensure an EMF vector file (.emf) is generated alongside the SVG.
    Uses LibreOffice, Inkscape, or cairosvg if available.
    """
    if output_emf is None:
        output_emf = svg_path.with_suffix(".emf")

    output_emf.parent.mkdir(parents=True, exist_ok=True)

    # 1. Try inkscape (best vector quality for SVG -> EMF)
    if shutil.which("inkscape"):
        cmd = ["inkscape", str(svg_path), "--export-filename=" + str(output_emf)]
        proc = subprocess.run(cmd, capture_output=True)
        if proc.returncode == 0 and output_emf.is_file():
            return True

    # 2. Try libreoffice / soffice
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if soffice:
        cmd = [
            soffice,
            "--headless",
            "--convert-to",
            "emf",
            str(svg_path),
            "--outdir",
            str(output_emf.parent),
        ]
        proc = subprocess.run(cmd, capture_output=True)
        converted = output_emf.parent / f"{svg_path.stem}.emf"
        if converted.is_file():
            if converted != output_emf:
                shutil.move(str(converted), str(output_emf))
            return True

    print("Warning: Neither inkscape nor libreoffice available for SVG -> EMF conversion", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Fireworks Tech Graph Bridge for PPT Master")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Check
    check_p = subparsers.add_parser("check", help="Check SVG geometry and XML using fireworks")
    check_p.add_argument("svg_file", type=Path, help="SVG file to check")

    # Render
    render_p = subparsers.add_parser("render", help="Render SVG from fireworks template")
    render_p.add_argument("template", type=str, help="Template name (e.g. architecture, agent-architecture, data-flow)")
    render_p.add_argument("output", type=Path, help="Output SVG path")
    render_p.add_argument("spec", type=str, help="JSON spec for nodes, arrows, etc.")

    # Export EMF
    emf_p = subparsers.add_parser("export-emf", help="Export SVG to EMF vector file")
    emf_p.add_argument("svg_file", type=Path, help="Source SVG file")
    emf_p.add_argument("output_emf", type=Path, nargs="?", default=None, help="Output EMF path")

    args = parser.parse_args()

    if args.command == "check":
        res = run_fireworks_check(args.svg_file)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 1

    elif args.command == "render":
        ok = render_from_template(args.template, args.output, args.spec)
        return 0 if ok else 1

    elif args.command == "export-emf":
        ok = export_emf(args.svg_file, args.output_emf)
        return 0 if ok else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
