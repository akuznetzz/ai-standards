# Core Rules

## Language & Communication
- Chat with the user in Russian.
- Keep code comments, docstrings, user-facing string literals, and git commit messages in English.

## Engineering Workflow
- Verify information before stating it.
- Preserve existing behavior unless the user explicitly requests a change.
- Make minimal, focused edits and avoid unrelated cleanup.
- Do not propose whitespace-only changes.
- Do not invent changes beyond the user's request.
- Prefer single coherent patches per file.

## Completion Discipline
- Do not mark work complete without verifying the result in a task-appropriate way.
- If verification is partial or unavailable, state that explicitly and name the remaining risk.
- For bug fixes, prefer confirming the root cause or the most likely failure path before closing the task.

## General Engineering Principles
- Prefer small, coherent changes.
- Keep functions small and single-purpose.
- Use meaningful names and avoid unclear abbreviations.
- Replace magic values with named constants or configuration.
- Keep file and module structure coherent and predictable.
- Hide implementation details behind clear interfaces and module boundaries.
- Use comments only to explain intent or non-obvious decisions.
- Refactor early when debt becomes visible.
- Add or update focused tests for bug fixes, edge cases, and error paths when the project has testing in place.

## DRY
- Do not duplicate code.
- If duplication is detected or strongly suspected, tell the user and propose a refactoring path.
