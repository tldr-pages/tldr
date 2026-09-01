# dolt diff

> Show changes between commits, the working tree, and staged tables in a Dolt repository.
> See also: `dolt-log`.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-diff>.

- Show unstaged changes:

`dolt diff`

- Show changes for specific tables:

`dolt diff {{table_name}}`

- Show changes between the working tree and a specific commit:

`dolt diff {{commit}}`

- Show changes between two commits:

`dolt diff {{commit1}} {{commit2}}`

- Show changes against the merge base of a branch:

`dolt diff --merge-base {{branch_name}}`
