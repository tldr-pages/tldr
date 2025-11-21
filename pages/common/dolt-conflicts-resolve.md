# dolt conflicts resolve

> Resolve merge conflicts in Dolt databases.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-conflicts-resolve>.

- Resolve conflicts by taking the current version (ours):

`dolt conflicts resolve --ours {{table_name}}`

- Resolve conflicts by taking the incoming version (theirs):

`dolt conflicts resolve --theirs {{table_name}}`

- Resolve conflicts by taking both versions:

`dolt conflicts resolve --both {{table_name}}`
