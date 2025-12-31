# git branch

> Main Git command for working with branches.
> More information: <https://git-scm.com/docs/git-branch>.

- List all branches (local and remote; the current branch is highlighted by `*`):

`git branch {{[-a|--all]}}`

- List which branches include a specific Git commit in their history:

`git branch {{[-a|--all]}} --contains {{commit_hash}}`

- Show the name of the current branch:

`git branch --show-current`

- Create new branch based on the current commit:

`git branch {{branch_name}}`

- Create new branch based on a specific commit:

`git branch {{branch_name}} {{commit_hash}}`

- Rename a branch (you must switch to a different branch before doing this):

`git branch {{[-m|--move]}} {{old_branch_name}} {{new_branch_name}}`

- Delete a local branch (you must switch to a different branch before doing this):

`git branch {{[-d|--delete]}} {{branch_name}}`

- Delete a remote branch:

`git push {{remote_name}} {{[-d|--delete]}} {{remote_branch_name}}`
