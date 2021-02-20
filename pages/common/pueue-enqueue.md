# pueue enqueue

> Enqueue stashed tasks.
> See also: `pueue stash`.
> More information: <https://github.com/Nukesor/pueue>.

- Enqueue multiple stashed tasks at once:

`pueue enqueue {{first task ID}} {{second task ID}} ...`

- Enqueue a stashed task after 60 seconds:

`pueue enqueue -d 60 {{task ID}}`

- Enqueue a stashed task next wednesday:

`pueue enqueue -d wednesday {{task ID}}`

- Enqueue a stashed task after four months:

`pueue enqueue -d "4 months" {{task ID}}`

- Enqueue a stashed task on 2025-02-08:

`pueue enqueue -d 2025-02-08 {{task ID}}`

- See all formats acceptable by -d:

`pueue enqueue --help`
