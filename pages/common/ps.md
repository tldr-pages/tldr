# ps

> Information about running processes.

- List all running processes:

`ps aux`

- List all running processes including the full command string:

`ps auxww`

- Search for a process that matches a string:

`ps aux | grep {{string}}`

- List all processes of the current user in extra full format:

`ps --user $(id --user) -F`

- List all processes of the current user as ASCII art process hierarchy:

`ps --user $(id --user) f`
