# dolt conflicts

> Manage table conflicts in a Dolt database.
> Conflicts can occur when merging branches with incompatible changes.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-conflicts>.

- List all tables with conflicts:

`dolt conflicts`

- View conflicts for a specific table:

`dolt conflicts {{table_name}}`

- Resolve conflicts by accepting the changes from the current branch (ours):

`dolt conflicts resolve --ours {{table_name}}`

- Resolve conflicts by accepting the changes from the merging branch (theirs):

`dolt conflicts resolve --theirs {{table_name}}`
