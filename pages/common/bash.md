# bash

> Bourne-Again SHell.
> `sh`-compatible command line interpreter.
> More information: <https://gnu.org/software/bash>.

- Start interactive shell:

`bash`

- Execute a command:

`bash -c "{{command}}"`

- Run commands from a file:

`bash {{file.sh}}`

- Run commands from a file, logging all commands executed to the terminal:

`bash -x {{file.sh}}`

- Run commands from a file, stopping at the first error:

`bash -e {{file.sh}}`

- Run commands from `stdin`:

`bash -s`

- Print the version information of bash (use `echo $BASH_VERSION` to show just the version string):

`bash --version`
