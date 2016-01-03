# lsof

> list open files
> Note: In most case, you need root privilege (or sudo) because you want to list files opened by other than you.

- list files opened by user

`lsof -u {{username}}`

- list processes that open specific file

`lsof {{file name}}`

- list files that open specific port

`lsof -i:{{port number}}`

- list files opened by command (or process) name (e.x nginx)

`lsof -c {{process_or_command_name}}`

- list files opened by PID

`lsof -p {{pid}}`
