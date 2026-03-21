# lsof

> List open files and the processes that opened them.
> More information: <https://manned.org/lsof>.

- List all open files:

`lsof`

- List all open files by a specific process:

`lsof -p {{pid}}`

- List all files opened by a specific user:

`lsof -u {{username}}`

- List all open network connections:

`lsof -i`

- List all open files on a specific port:

`lsof -i :{{port}}`

- List all open files in a specific directory:

`lsof +D {{/path/to/directory}}`
