# bash-histexpand

> Reuse and expand your bash history.
> More information: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction.html>.

- Run the previous command:

`!!`

- Run the previous command as root:

`sudo !!`

- Run a command with the last argument of the previous command:

`{{command}} !$`

- Run a command with the first argument of the previous command:

`{{command}} !^`

- Run a command `n` lines back in the history:

`!-{{n}}`

- Run the most recent command starting with `string`:

`!{{string}}`

- Run the previous command, replacing `string1` with `string2`:

`^{{string1}}^{{string2}}^`

- Print a command `n` lines back without running it:

`!-{{n}}:p`
