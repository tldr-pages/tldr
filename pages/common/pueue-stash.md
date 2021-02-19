# pueue stash

> Stash tasks to prevent automatic start.
> see also: pueue start --help
> see also: pueue enqueue --help

- stash an enqueued task

`pueue stash {{task ID}}`

- stash multiple tasks at once 

`pueue stash {{first task ID}} {{second task ID}} ...`

- start a stashed task immediately

`pueue start {{task ID}}`

- enqueue a task, to be executed when preceding tasks finish

`pueue enqueue {{task ID}}`
