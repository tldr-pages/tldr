# jj operation

> Work with the operation log of a `jj` repository.
> Some subcommands such as `abandon`, `diff`, `integrate`, `log`, `restore`, `revert`, `show` have their own usage documentation.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation>.

- Show operation log:

`jj {{[op|operation]}} log`

- Abandon a specific operation:

`jj {{[op|operation]}} abandon {{operation}}`

- Restore the repository to its state at a given operation:

`jj {{[op|operation]}} restore {{operation}}`

- Revert an earlier operation by applying its inverse:

`jj {{[op|operation]}} revert {{operation}}`

- Show changes to the repository in an operation:

`jj {{[op|operation]}} show {{operation}}`

- Show stat, summary, and patch of modifications of an operation:

`jj {{[op|operation]}} show {{--stat}} {{[-s|--summary]}} {{[-p|--patch]}} {{operation}}`

- Compare repository changes between two operations:

`jj {{[op|operation]}} diff {{[-f|--from]}} {{from_op}} {{[-t|--to]}} {{to_op}}`

- Show diff as a histogram of changes:

`jj {{[op|operation]}} diff {{--stat}} {{[--op|--operation]}} {{operation_id}}`