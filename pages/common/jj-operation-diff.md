# jj operation diff

> Compare changes to the repository between two operations.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-diff>.

- Compare repository changes in a specific operation to its parent:

`jj {{[op|operation]}} diff {{[--op|--operation]}} {{operation_id}}`

- Compare repository changes between two specific operations:

`jj {{[op|operation]}} diff {{[-f|--from]}} {{from_op}} {{[-t|--to]}} {{to_op}}`

- Show diff with a patch of modifications to changes:

`jj {{[op|operation]}} diff {{[-p|--patch]}} {{[--op|--operation]}} {{operation_id}}`

- Show diff as a histogram of changes:

`jj {{[op|operation]}} diff --stat {{[--op|--operation]}} {{operation_id}}`

- Show diff without a graph:

`jj {{[op|operation]}} diff {{[-G|--no-graph]}} {{[--op|--operation]}} {{operation_id}}`
