# history expansion

> Reuse and expand the shell history in `sh`, `bash`, `zsh`, `rbash` and `ksh`.
> More information: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Run the previous command:

`!!`

- Run the previous command as root:

`sudo !!`

- Run a command with the last argument of the previous command:

`{{command}} !$`

- Run a command with the first argument of the previous command:

`{{command}} !^`

- Run the command `n` lines back in the history:

`!-{{n}}`

- Run the most recent command starting with `string`:

`!{{string}}`

- Run the previous command, replacing `string1` with `string2`:

`^{{string1}}^{{string2}}^`

- Perform a history expansion, but print the command that would be run instead of actually running it:

`{{!-n}}:p`
