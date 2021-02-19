# pueue log

> Display the log output tasks.
> see also: pueue status --help

- show the last few lines of output from all tasks

`pueue log`

- show full output of a specific task

`pueue log {{task ID}}`

- show last few lines of output from several commands.

`pueue log {{first task ID}} {{second task ID}} ...`

- print a specific number of lines from the tail of output.

`pueue log -l {{number of lines}} {{task ID}}`
