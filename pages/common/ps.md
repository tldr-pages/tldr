# ps

> Information about running processes.
> More information: <https://manned.org/ps>.

- List all running processes:

`ps aux`

- List all running processes including the full command string:

`ps auxww`

- Search for a process that matches a string (the brackets will prevent `grep` from matching itself):

`ps aux | grep {{[s]tring}}`

- List all processes of the current user in extra full format:

`ps --user $(id -u) -F`

- List all processes of the current user as a tree:

`ps --user $(id -u) f`

- Get the parent PID of a process:

`ps -o ppid= -p {{pid}}`

- Sort processes by memory consumption:

`ps --sort size`
