# pueue stash

> Stash tasks to prevent automatic start.
> See also: `pueue start`.
> See also: `pueue enqueue`.
> More information: <https://github.com/Nukesor/pueue>.

- Stash an enqueued task:

`pueue stash {{task ID}}`

- Stash multiple tasks at once:

`pueue stash {{first task ID}} {{second task ID}} ...`

- Start a stashed task immediately:

`pueue start {{task ID}}`

- Enqueue a task, to be executed when preceding tasks finish:

`pueue enqueue {{task ID}}`
