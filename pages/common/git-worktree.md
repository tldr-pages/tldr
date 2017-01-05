# git worktree

> Manage multiple working trees attached to the same repository.

- Create a new folder with the specified branch checked out into it:

`git worktree add {{path}} {{branch}}`

- List all the working directories attached to this repo:

`git worktree list`

- Create a new folder with a new branch checked out into it:

`git worktree add -b {{new_branch}} {{path}}`
