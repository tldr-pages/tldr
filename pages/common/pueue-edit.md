# pueue edit

> Edit the command or path of a stashed or queued task.
> More information: <https://github.com/Nukesor/pueue>.

- Edit the command with ID 2, see 'pueue status --help' to get command ID:

`pueue edit 2`

- Edit the path from which a task is executed:

`pueue edit {{task_id}} --path`

- Edit a command with your favourite editor:

`EDITOR=nano pueue edit 11`
