# pueue enqueue

> Enqueue stashed tasks.
> see also: pueue stash --help

- enqueue multiple stashed tasks at once

`pueue enqueue {{first task ID}} {{second task ID}} ...`

- enqueue a stashed task after 60 seconds

`pueue enqueue -d 60 {{task ID}}`

- enqueue a stashed task next wednesday

`pueue enqueue -d wednesday {{task ID}}`

- enqueue a stashed task after four months

`pueue enqueue -d "4 months" {{task ID}}`

- enqueue a stashed task on 2025-02-08

`pueue enqueue -d 2025-02-08 {{task ID}}`

- see all formats acceptable by -d

`pueue enqueue --help`
