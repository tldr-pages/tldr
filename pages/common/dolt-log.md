# dolt log

> Show the commit history of a Dolt repository.
> See also: `dolt-diff`.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-log>.

- Show the commit history of the current branch:

`dolt log`

- Show a limited number of recent commits:

`dolt log -n {{count}}`

- Show the commit history for a specific table:

`dolt log -- {{table_name}}`

- Show the commit history of a table up to a specific commit:

`dolt log {{commit}} -- {{table_name}}`

- Show commits reachable from a specific commit, excluding those reachable from another:

`dolt log {{commit}} --not {{exclude_commit}}`
