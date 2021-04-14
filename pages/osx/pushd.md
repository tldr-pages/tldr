# pushd

> Place a directory on a stack so it can be accessed later.
> See also `popd` to switch back to original directory and `dirs` to display directory stack contents.

- Switch to directory and push it on the stack:

`pushd {{directory}}`

- Switch first and second directories on the stack:

`pushd`

- Rotate stack by making the 5th element the top of the stack:

`pushd +4`
