# pueue log

> Display the log output tasks.
> See also: `pueue status`.
> More information: <https://github.com/Nukesor/pueue>.

- Show the last few lines of output from all tasks:

`pueue log`

- Show full output of a specific task:

`pueue log {{task ID}}`

- Show last few lines of output from several commands:

`pueue log {{first task ID}} {{second task ID}} ...`

- Print a specific number of lines from the tail of output:

`pueue log --lines {{number_of_lines}} {{task_id}}`
