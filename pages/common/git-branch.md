# git branch

> Main git command for working with branches.

- List local branches. The current branch is highlighted by `*`:

`git branch`

- List all branches (local and remote):

`git branch -a`

- Create new branch based on the current commit:

`git branch {{branch_name}}`

- Rename a branch (must not have it checked out to do this):

`git branch -m {{old_branch_name}} {{new_branch_name}}`

- Delete a local branch:

`git branch -d {{branch_name}}`
