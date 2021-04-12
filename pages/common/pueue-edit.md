# pueue edit

> Edit the command or path of a stashed or queued task.
> More information: <https://github.com/Nukesor/pueue>.

- Edit a task, see `pueue status` to get the task ID:

`pueue edit {{task_id}}`

- Edit the path from which a task is executed:

`pueue edit {{task_id}} --path`

- Edit a command with the specified editor:

`EDITOR={{nano}} pueue edit {{task_id}}`
