---
name: pr-description
description: Write a clear pull request title and description from the current branch diff. Use when the user asks for a PR description or summary of changes.
---

# PR description

1. Run `git log main..HEAD --oneline` and `git diff main...HEAD --stat`, then read the diff for the important files (use the repo's real default branch).
2. Output:
   - **Title**: under 70 characters, imperative mood.
   - **Why**: the problem or goal in 1-3 sentences.
   - **What changed**: bullets grouped by behavior, not by file.
   - **How to test**: exact commands or steps.
   - **Risks / follow-ups**: migrations, config, breaking changes, known gaps.
3. State only what the diff shows. If the motivation is not visible, ask instead of inventing it.
