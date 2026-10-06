#!/usr/bin/env python3
"""ccaudit: estimate how many tokens your Claude Code project config costs every session.

Usage: python3 ccaudit.py [project_dir]
Token estimate is chars/4 (rough). No network, no dependencies.
"""
import json, sys
from pathlib import Path

def est(text): return max(1, len(text) // 4)

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    rows = []
    for name in ("CLAUDE.md", ".claude/CLAUDE.md", "CLAUDE.local.md"):
        p = root / name
        if p.is_file():
            t = p.read_text(errors="ignore")
            rows.append((name, est(t), f"{len(t.splitlines())} lines"))
    # skills: only name+description are preloaded; body loads on invoke
    for d in (root / ".claude" / "skills", Path.home() / ".claude" / "skills"):
        if d.is_dir():
            for s in sorted(d.glob("*/SKILL.md")):
                t = s.read_text(errors="ignore")
                head = t.split("---")[1] if t.startswith("---") and t.count("---") >= 2 else t[:300]
                rows.append((f"skill:{s.parent.name}", est(head), f"body {est(t)} tok when invoked"))
    mcp = root / ".mcp.json"
    if mcp.is_file():
        try:
            n = len(json.loads(mcp.read_text()).get("mcpServers", {}))
            rows.append((f".mcp.json ({n} servers)", n * 4000, "rough: ~4k tok/server of tool schemas"))
        except Exception as e:
            rows.append((".mcp.json", 0, f"unreadable: {e}"))
    total = sum(r[1] for r in rows)
    print(f"{'item':40} {'tokens':>8}  note")
    for n, t, note in rows:
        print(f"{n:40} {t:>8}  {note}")
    print(f"{'TOTAL per session':40} {total:>8}")
    for n, t, _ in rows:
        if n.endswith("CLAUDE.md") and t > 1500:
            print(f"WARN: {n} is ~{t} tokens; move procedures into skills, keep it under ~100 lines.")
    if total == 0:
        print("Nothing found. Run from a project root.")

if __name__ == "__main__":
    main()
