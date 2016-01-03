# lsof

> Lists open files and the corresponding processes
> Note: In most case, you need root privilege (or sudo) because you want to list files opened by other than you.

- find the processes that have a given file open

`lsof {{/path/to/file}}`

- find the process that opened a local internet port

`lsof -i :{{8080}}`

- only output the process PID (e.g. to pipe into kill)

`lsof -t {{/path/to/file}} | xargs kill -9`

- list files opened by user

`lsof -u {{username}}`

- list files opened by command (or process) name (e.x nginx)

`lsof -c {{process_or_command_name}}`
