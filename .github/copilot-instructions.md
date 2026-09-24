# Copilot instructions for this repository

## Project purpose

This project is a small Python utility that renames files in a directory by normalizing names to lowercase, replacing spaces and punctuation with hyphens, and preserving the original folder structure. Keep the tool simple, predictable, and cross-platform.

## Coding conventions

See [instructions/conventions.instructions.md](instructions/conventions.instructions.md) for detailed Python conventions standards.

## Testing expectations

- Add or update pytest coverage for behavioral changes.
- Prefer writing a failing test before implementing a fix, then keep the fix minimal.
- Tests should validate real behavior, especially path normalization, rename logic, and interactive/non-interactive main flow.
- Before concluding work, run the relevant pytest checks for the touched behavior.

## Implementation guidance

- Match the current project style: snake_case functions, straightforward control flow, and minimal abstraction.
- When changing file naming rules, preserve the existing normalization semantics and update tests accordingly.
- Keep path logic deterministic and avoid platform-specific assumptions beyond the already-supported `os` and `pathlib` usage.
- If the task involves interactive prompts, keep the prompts and user choices consistent with the current user experience.

## Review checklist

- Did the change keep the tool simple and dependency-free?
- Did it preserve path and directory behavior across platforms?
- Did tests cover the modified behavior and pass?
- Did the fix remain scoped to the task rather than broadening the project unnecessarily?
