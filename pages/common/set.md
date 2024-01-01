# set

> Toggle shell options or set the values of positional parameters.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#set>.

- Display the names and values of shell variables:

`set`

- Export newly initialized variables to child processes:

`set -a`

- Write formatted messages to `stderr` when jobs finish:

`set -b`

- Write and edit text in the command line with `vi`-like keybindings (e.g. `yy`):

`set -o {{vi}}`

- Exit the shell when (some) commands fail:

`set -e`
