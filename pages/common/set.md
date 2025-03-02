# set

> Toggle shell options or set the values of positional parameters.
> More information: <https://manned.org/set.1posix>.

- Display the names and values of shell variables:

`set`

- Export newly initialized variables to child processes:

`set -a`

- Write formatted messages to `stderr` when jobs finish:

`set -b`

- Write and edit text in the command-line with `vi`-like keybindings (e.g. `yy`):

`set -o {{vi}}`

- Return to default mode:

`set -o {{emacs}}`

- List all modes:

`set -o`

- Exit the shell when (some) command fails:

`set -e`

- Reset all shell parameters and assign new ones:

`set -- {{argument1 argument2 ...}}`
