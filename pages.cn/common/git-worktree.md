# git worktree

> Manage multiple working trees attached to the same repository.

- Create a new folder with the specified branch checked out into it:

`git worktree add {{path/to/folder}} {{branch}}`

- Create a new folder with a new branch checked out into it:

`git worktree add {{path/to/folder}} -b {{new_branch}}`

- List all the working directories attached to this repository:

`git worktree list`

- Remove a worktree (after deleting worktree folder):

`git worktree prune`
