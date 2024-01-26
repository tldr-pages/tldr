# bash

> Bourne-Again SHell, an `sh`-compatible command-line interpreter.
> See also: `zsh`, `histexpand` (history expansion).
> More information: <https://www.gnu.org/software/bash/>.

- Start an interactive shell session:

`bash`

- Start an interactive shell session without loading startup configs:

`bash --norc`

- Execute specific [c]ommands:

`bash -c "{{echo 'bash is executed'}}"`

- Execute a specific script:

`bash {{path/to/script.sh}}`

- E[x]ecute a specific script, printing each command before executing it:

`bash -x {{path/to/script.sh}}`

- Execute a specific script and stop at the first [e]rror:

`bash -e {{path/to/script.sh}}`

- Execute specific commands from `stdin`:

`{{echo "echo 'bash is executed'"}} | bash`

- Start a [r]estricted shell session:

`bash -r`
