# git reset

> Undo commits or unstage changes, by resetting the current git HEAD to the specified state.

- Undo last commit, keep the changes in the local filesystem:

`git reset HEAD~1`

- Undo last commit, permanently delete the changes, and discard staged changes:

`git reset --hard HEAD~1`
