# dolt branch

> Manage Dolt branches.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-branch>.

- List local branches (current branch is highlighted by `*`):

`dolt branch`

- List all local and remote branches:

`dolt branch --all`

- Create a new branch based on the current branch:

`dolt branch {{branch_name}}`

- Create a new branch with the specified commit as the latest:

`dolt branch {{branch_name}} {{commit}}`

- Rename a branch:

`dolt branch --move {{branch_name1}} {{branch_name2}}`

- Duplicate a branch:

`dolt branch --copy {{branch_name1}} {{branch_name2}}`

- Delete a branch:

`dolt branch --delete {{branch_name}}`

- Display the name of the current branch:

`dolt branch --show-current`
