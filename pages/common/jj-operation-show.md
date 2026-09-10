# jj operation show

> Show repository changes in an operation.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-show>.

- Show repository changes in the current operation compared to its parent:

`jj {{[op|operation]}} show`

- Show repository changes in a specific operation:

`jj {{[op|operation]}} show {{operation_id}}`

- Show repository changes with patch details:

`jj {{[op|operation]}} show {{[-p|--patch]}} {{operation_id}}`

- Show a summary of changed paths in an operation:

`jj {{[op|operation]}} show {{[-s|--summary]}} {{operation_id}}`

- Show a histogram of changes in an operation:

`jj {{[op|operation]}} show --stat {{operation_id}}`

- Show changes without a graph:

`jj {{[op|operation]}} show {{[-G|--no-graph]}} {{operation_id}}`
