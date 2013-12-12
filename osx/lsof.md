# lsof

> Lists open files and the corresponding processes

- find the processes that have a given file open

`lsof {{/path/to/file}}`

- find the process that opened a local internet port

`lsof -i :{{8080}}`

- only output the process PID (e.g. to pipe into kill)

`lsof -t {{/path/to/file}} | xargs kill -9`
