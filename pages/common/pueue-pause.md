# pueue pause

> pause running tasks or groups.
> see also: pueue start --help

- pause all tasks in the default group

`pueue pause`

- pause a running task

`pueue pause {{task ID}}`

- pause a running task and stop all its direct [c]hildren.

`pueue pause -c {{task ID}}`

- pause all tasks in a [g]roup and prevent it from starting new tasks.

`pueue pause -g {{group name}}`

- pause [a]ll tasks and prevent all groups from starting new tasks.

`pueue pause -a`
