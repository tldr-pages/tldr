# pueue pause

> Pause running tasks or groups.
> See also: `pueue start`.
> More information: <https://github.com/Nukesor/pueue>.

- Pause all tasks in the default group:

`pueue pause`

- Pause a running task:

`pueue pause {{task ID}}`

- Pause a running task and stop all its direct [c]hildren:

`pueue pause -c {{task ID}}`

- Pause all tasks in a [g]roup and prevent it from starting new tasks:

`pueue pause -g {{group name}}`

- Pause [a]ll tasks and prevent all groups from starting new tasks:

`pueue pause -a`
