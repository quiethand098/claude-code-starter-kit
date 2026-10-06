# [Project name]

[One sentence: what this does.]

## Commands
- Install: `pnpm install`
- Dev: `pnpm dev`
- Test all: `pnpm test`
- Test one: `pnpm vitest run path/to/file.test.ts -t "name"`
- Typecheck: `pnpm tsc --noEmit`
- Lint: `pnpm lint --fix`

## Layout
- `src/` source, `src/[domain]/` per feature, tests next to code as `*.test.ts`.

## Conventions
- TypeScript strict. No `any`; use `unknown` and narrow.
- ES modules, named exports, no default exports.
- Validate external input at the boundary (zod or equivalent).
- No new dependencies without asking.

## Workflow
- Typecheck and run affected tests before declaring done.
- Do not touch `[dist/, lockfile]` by hand.
- Small commits, imperative messages ("Add retry to fetcher").
