# bash

> Bourne-Again SHell, an `sh`-compatible command line interpreter.
> See also `histexpand` for history expansion.
> More information: <https://gnu.org/software/bash/>.

- Start an interactive shell session:

`bash`

- Execute a command and then exit:

`bash -c "{{command}}"`

- Execute a script:

`bash {{path/to/script.sh}}`

- Execute a script, printing each command before executing it:

`bash -x {{path/to/script.sh}}`

- Execute commands from a script, stopping at the first error:

`bash -e {{path/to/script.sh}}`

- Read and execute commands from stdin:

`bash -s`

- Print the Bash version (`$BASH_VERSION` contains the version without license information):

`bash --version`
