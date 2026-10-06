# Claude Code Starter Kit (free edition)

Ready-to-use `CLAUDE.md` templates and 5 project skills for Claude Code. Copy, edit the bracketed parts, ship.

## Contents
- `claude-md-templates/` — Python and TypeScript/Node templates.
- `skills/` — bug-hunt, test-first, pr-description.

## Install
1. Copy a template to your repo root as `CLAUDE.md`. Replace every `[bracketed]` item.
2. Copy a skill folder into `.claude/skills/` (project) or `~/.claude/skills/` (global).
3. Invoke by name, e.g. `/bug-hunt the checkout total is off by one cent`.

## Tips
- Keep CLAUDE.md under ~100 lines. Every line is paid for in tokens on every session.
- Write commands exactly as you run them. Claude cannot guess your test runner flags.
- Put rules you keep repeating into CLAUDE.md; put multi-step procedures into skills.

## License
MIT
