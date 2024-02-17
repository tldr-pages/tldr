# ps

> Information about running processes.
> More information: <https://keith.github.io/xcode-man-pages/ps.1.html>.

- List all running processes:

`ps aux`

- List all running processes including the full command string:

`ps auxww`

- Search for a process that matches a string:

`ps aux | grep {{string}}`

- Get the parent PID of a process:

`ps -o ppid= -p {{pid}}`

- Sort processes by memory usage:

`ps -m`

- Sort processes by CPU usage:

`ps -r`
