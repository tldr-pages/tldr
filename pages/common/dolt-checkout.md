# dolt checkout

> Checkout the work tree or tables to a specific branch or commit.
> More information: <https://github.com/dolthub/dolt>.

- Switch to a branch:

`dolt checkout {{branch_name}}`

- Revert unstaged changes to a table:

`dolt checkout {{table}}`

- Create new branch and switch to it:

`dolt checkout -b {{branch_name}}`

- Create new branch based on a specified commit and switch to it:

`dolt checkout -b {{branch_name}} {{commit}}`
