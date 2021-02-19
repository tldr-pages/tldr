# pueue kill

> Kill running tasks or whole groups.

- Kill all tasks in the default group:

`pueue kill`

- Kill a specific task by ID:

`pueue kill {{task ID}}`

- Kill a task and terminate all its [c]hildren processes:

`pueue kill -c {{task ID}}`

- Kill all tasks in a [g]roup and pause the group:

`pueue kill -g {*{*group name}}`

- Kill [a]ll tasks across all groups and pause all groups:

`pueue kill -a`
