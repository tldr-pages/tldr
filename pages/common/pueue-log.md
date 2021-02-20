# pueue log

> Display the log output tasks.
> See also: `pueue status`.
> More information: <https://github.com/Nukesor/pueue>.

- Show the last few lines of output from all tasks:

`pueue log`

- Show full output of a task:

`pueue log {{task_id}}`

- Show last few lines of output from several tasks:

`pueue log {{task_id}} {{task_id}}`

- Print a specific number of lines from the tail of output:

`pueue log --lines {{number_of_lines}} {{task_id}}`
