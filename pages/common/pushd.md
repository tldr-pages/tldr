# pushd

> Place a directory on a stack so it can be accessed later.
> See also `popd` to switch back to original directory and `dirs` to display directory stack contents.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Switch to directory and push it on the stack:

`pushd {{path/to/directory}}`

- Switch first and second directories on the stack:

`pushd`

- Rotate stack by making the 5th element the top of the stack:

`pushd +4`

- Rotate the stack 4 times to the left (the current directory stays at the top by replacing the 5th element):

`pushd -n +4`
