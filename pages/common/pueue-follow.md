# pueue follow

> Follow the output of a currently running task.
> See also: `pueue log`.
> More information: <https://github.com/Nukesor/pueue>.

- Follow the output of a task (`stdout` + `stderr`):

`pueue follow {{task_id}}`

- Follow `stderr` of a task:

`pueue follow --err {{task_id}}`
