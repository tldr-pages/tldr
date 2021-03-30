# pueue start

> Resume operation of specific tasks or groups of tasks.
> See also: `pueue pause`.
> More information: <https://github.com/Nukesor/pueue>.

- Resume all tasks in the default group:

`pueue start`

- Resume a specific task:

`pueue start {{task_id}}`

- Resume multiple tasks at once:

`pueue start {{task_id}} {{task_id}}`

- Resume all tasks and start their children:

`pueue start --all --children`

- Resume all tasks in a specific group:

`pueue start group {{group_name}}`
