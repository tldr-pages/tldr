# lsof

> Lists open files and the corresponding processes
> Note: In most cases, you need root privilege (or use sudo) because you want to list files opened by others

- find the processes that have a given file open

`lsof {{/path/to/file}}`

- find the process that opened a local internet port

`lsof -i :{{port}}`

- only output the process PID

`lsof -t {{/path/to/file}}`

- list files opened by the given user

`lsof -u {{username}}`

- list files opened by the given command or process

`lsof -c {{process_or_command_name}}`
