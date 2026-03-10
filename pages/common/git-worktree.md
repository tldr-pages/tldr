# git worktree

> Manage multiple working trees attached to the same repository.
> More information: <https://git-scm.com/docs/git-worktree>.

- Add a new worktree directory for a branch with the same name (created if missing):

`git worktree add {{branch}}`

- Create a new directory with the specified branch checked out into it:

`git worktree add {{path/to/directory}} {{branch}}`

- Create a new directory with a new branch checked out into it:

`git worktree add {{path/to/directory}} -b {{new_branch}}`

- List all the working directories (including the primary one):

`git worktree list`

- Move an existing worktree to a new location:

`git worktree move {{path/to/worktree}} {{new/path}}`

- Remove a worktree directory and its metadata (only if it has no uncommitted changes):

`git worktree remove {{path/to/worktree}}`

- Remove metadata for a worktree directory that's been manually deleted:

`git worktree prune`
