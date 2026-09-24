---
applyTo: "**/*.py"
description: "Python conventions standards and best practices"
---

## Coding conventions

- Prefer the Python standard library over third-party packages.
- Keep code readable and explicit; favor small functions and clear naming.
- Use type annotations for function signatures and local variables where they already fit the project style.
- Keep file-handling logic robust for both Windows and Unix path separators.
- Preserve the existing CLI flow and user confirmation behavior unless the task specifically requires changing it.
- Do not add unrelated refactors, framework changes, or dependencies.
