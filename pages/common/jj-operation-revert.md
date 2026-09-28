# jj operation revert

> Revert an earlier operation by applying its inverse in a `jj` repository.
> See also: `jj operation log`, `jj operation restore`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-revert>.

- Revert the most recent operation:

`jj {{[op|operation]}} revert`

- Revert a specific operation:

`jj {{[op|operation]}} revert {{operation_id}}`

- Revert only the repository state and local bookmarks of an operation:

`jj {{[op|operation]}} revert --what repo {{operation_id}}`
