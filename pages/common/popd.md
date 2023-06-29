# popd

> Remove a directory placed on the directory stack via the pushd shell built-in.
> See also `pushd` to place a directory on the stack and `dirs` to display directory stack contents.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Remove the top directory from the stack and cd to it:

`popd`

- Remove the Nth directory (from the left of the list printed with `dirs`), couting starts at zero:

`popd +N`

- Remove the Nth directory (from the right of the list printed with `dirs`), counting starts at zero:

`popd -N`

- Remove the 1st directory (from the left of the list printed with `dirs`), counting starts at zero:

`popd -n`
