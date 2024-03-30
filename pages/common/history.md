# history

> Command-line history.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Display the commands history list with line numbers:

`history`

- Display the last 20 commands (in Zsh it displays all commands starting from the 20th):

`history {{20}}`

- Clear the commands history list (only for current Bash shell):

`history -c`

- Overwrite history file with history of current Bash shell (often combined with `history -c` to purge history):

`history -w`

- Delete the history entry at the specified offset:

`history -d {{offset}}`
