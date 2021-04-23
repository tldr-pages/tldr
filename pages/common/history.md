# history

> Command Line history.
> More information: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Display the commands history list with line numbers:

`history`

- Display the last 20 commands:

`history {{20}}`

- Clear the commands history list (only for current `bash` shell):

`history -c`

- Overwrite history file with history of current `bash` shell (often combined with `history -c` to purge history):

`history -w`

- Delete the history entry at the specified offset:

`history -d {{offset}}`
