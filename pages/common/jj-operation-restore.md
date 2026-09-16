# jj operation restore

> Restore the repository to an earlier state in the operation log.
> See also: `jj undo`, `jj operation log`, `jj operation revert`, `jj operation show`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-restore>.

- Restore the repository state at a specific operation:

`jj {{[op|operation]}} restore {{operation_id}}`

- Restore only the repository state and local bookmarks (ignoring remote-tracking bookmarks):

`jj {{[op|operation]}} restore --what repo {{operation_id}}`
