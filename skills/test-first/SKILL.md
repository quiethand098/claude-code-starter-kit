---
name: test-first
description: Implement a feature or change test-first. Use when the user asks to add behavior that can be verified by automated tests.
---

# Test first

1. Restate the requested behavior as 3-6 concrete examples (input -> expected output), including one edge case and one failure case. Confirm with the user only if the examples are ambiguous.
2. Find the existing test style and runner in the repo; match it.
3. Write the tests. Run them and confirm they fail for the right reason.
4. Write the minimum code to pass. Run the tests again.
5. Refactor only if the code is clearly messy, rerunning tests after each step.
6. Run the whole suite. Report what was added and the final test output summary.
