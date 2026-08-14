# jj operation abandon

> Abandon operation history in a `jj` repository.
> See also: `jj operation log`, `jj operation restore`, `jj operation revert`
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-abandon>.

- Abandon a specific operation:

`jj {{[op|operation]}} abandon {{operation_id}}`

- Abandon a specific operation and all of its ancestors:

`jj {{[op|operation]}} abandon ..{{operation_id}}`

- Discard recent operations after restoring to an earlier state:

`jj {{[op|operation]}} abandon {{operation_id}}..@-`
