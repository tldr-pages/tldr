# jj operation log

> Show the operation log in a `jj` repository.
> See also: `jj operation abandon`, `jj operation diff`, `jj operation integrate`, `jj operation restore`, `jj operation revert`, `jj operation show`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-log>.

- Show the operation log:

`jj {{[op|operation]}} log`

- Limit the number of operations to show:

`jj {{[op|operation]}} log {{[-n|--limit]}} {{count}}`

- Show operations in reverse order (oldest first):

`jj {{[op|operation]}} log --reversed`

- Show operations without a graph:

`jj {{[op|operation]}} log {{[-G|--no-graph]}}`

- Render the operation log using a custom template:

`jj {{[op|operation]}} log {{[-T|--template]}} "{{template}}"`
