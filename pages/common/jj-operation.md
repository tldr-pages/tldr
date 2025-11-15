# jj operation

> Work with the operation log of a `jj` repository.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation>.

- Show operation log:

`jj {{[op|operation]}} log`

- Undo the last operation:

`jj {{[op|operation]}} undo`

- Undo a given operation:

`jj {{[op|operation]}} undo {{operation}}`

- Restore the repository to its state at a given operation:

`jj {{[op|operation]}} restore {{operation}}`

- Show changes to the repository in an operation:

`jj {{[op|operation]}} show {{operation}}`

- Show stat, summary and patch of modifications of an operation:

`jj {{[op|operation]}} show {{--stat}} {{[-s|--summary]}} {{[-p|--patch]}} {{operation}}`
