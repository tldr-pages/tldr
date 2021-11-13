# bash

> Bourne-Again SHell, an `sh`-compatible command-line interpreter.
> See also `histexpand` for history expansion.
> More information: <https://gnu.org/software/bash/>.

- Start an interactive shell session:

`bash`

- Start an interactive shell session without loading startup configs:

`bash --norc`

- Execute a [c]ommand:

`bash -c "{{command}}"`

- Execute a script:

`bash {{path/to/script.bash}}`

- Execute a script while printing each command before executing it:

`bash -x {{path/to/script.sh}}`

- Execute a script and stop at a first [e]rror:

`bash -e {{path/to/script.sh}}`

- Execute a command from [s]tdin:

`bash -s`

- Print the version:

`bash --version`
