# [Project name]

[One sentence: what this service/library does.]

## Commands
- Install: `uv sync`
- Test all: `uv run pytest -q`
- Test one: `uv run pytest tests/path.py::test_name -q`
- Lint/format: `uv run ruff check --fix . && uv run ruff format .`
- Types: `uv run mypy src`

## Layout
- `src/[pkg]/` application code; `tests/` mirrors it.
- [Name the 2-3 modules a newcomer must know and what each owns.]

## Conventions
- Python [3.12]. Type hints on all public functions.
- Prefer small pure functions; I/O at the edges.
- No new dependencies without asking. Prefer the standard library.
- Errors: raise specific exceptions, never bare `except:`.

## Workflow
- Run the single relevant test first, then the full suite before saying a task is done.
- Do not edit `[generated/ or migrations/]` by hand.
- Ask before changing public APIs or database schemas.
