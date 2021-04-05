# pueue enqueue

> Enqueue stashed tasks.
> See also: `pueue stash`.
> More information: <https://github.com/Nukesor/pueue>.

- Enqueue multiple stashed tasks at once:

`pueue enqueue {{task_id}} {{task_id}}`

- Enqueue a stashed task after 60 seconds:

`pueue enqueue --delay {{60}} {{task_id}}`

- Enqueue a stashed task next Wednesday:

`pueue enqueue --delay {{wednesday}} {{task_id}}`

- Enqueue a stashed task after four months:

`pueue enqueue --delay "4 months" {{task_id}}`

- Enqueue a stashed task on 2021-02-19:

`pueue enqueue --delay {{2021-02-19}} {{task_id}}`

- List all available date/time formats:

`pueue enqueue --help`
