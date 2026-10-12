---
name: count-tests
description: Use this skill when the user asks to count tests, summarize the test suite, or wants to know how many tests exist in the project.
---

# Count Tests

1. Execute [script](./scripts/count-tests.py) to count the number of tests in the project and gather relevant information about the test suite.

2. Parse the script's JSON output. Use the `total_files` and `total_tests` fields.

3. Respond using the [TEMPLATE](./TEMPLATE.md), filling in the values from the script output.
