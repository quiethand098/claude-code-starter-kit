---
name: bug-hunt
description: Systematically find and fix the root cause of a bug. Use when the user reports a failing test, wrong output, crash, or regression.
---

# Bug hunt

1. **Reproduce.** Get the exact failing command, input, and error. If you cannot reproduce it, say so and ask for details; do not guess.
2. **Narrow.** Find the smallest input or the first commit/line where behavior diverges. Prefer a failing test over manual poking.
3. **Hypothesize.** Write 2-3 candidate causes ranked by likelihood. Test the top one with a print, assertion, or debugger before editing code.
4. **Fix the cause, not the symptom.** Make the smallest change that makes the failing case pass. Do not refactor unrelated code.
5. **Lock it in.** Add a regression test that fails without the fix and passes with it.
6. **Verify.** Run the full relevant test suite. Report: root cause, the fix, the test added, anything still uncertain.
