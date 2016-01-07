# lsof

> Lists open files and the corresponding processes.

- Find the processes that have a given file open:

`lsof {{/path/to/file}}`

- Find the process that opened a local internet port:

`lsof -i :{{8080}}`

- Only output the process PID (e.g. to pipe into kill):

`lsof -t {{/path/to/file}} | xargs kill -9`
