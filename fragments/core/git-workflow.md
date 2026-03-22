## Git Workflow
- Never create commits on `main`, `master`, `develop`, or `staging`.
- If currently on one of those branches, warn the user and suggest creating a new branch.
- Always ask the user to approve the commit message text before committing.
- Extract the SCM task id from branch names shaped as `<purpose>/<task_id>-<description>`.
- Use commit messages in the form `task_id. (commit_type) commit_message.`

