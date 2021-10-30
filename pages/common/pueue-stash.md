# pueue stash

> Stash tasks to prevent them starting automatically.
> See also `pueue start` and `pueue enqueue`.
> More information: <https://github.com/Nukesor/pueue>.

- Stash an enqueued task:

`pueue stash {{task_id}}`

- Stash multiple tasks at once:

`pueue stash {{task_id}} {{task_id}}`

- Start a stashed task immediately:

`pueue start {{task_id}}`

- Enqueue a task to be executed when preceding tasks finish:

`pueue enqueue {{task_id}}`
