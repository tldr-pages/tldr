# pueue kill

> Kill running tasks or whole groups.

- kill all tasks in the default group.

`pueue kill`

- kill a specific task by ID.

`pueue kill {{task ID}}`

- kill a task and terminate all its [c]hildren processes.

`pueue kill -c {{task ID}}`

- kill all tasks in a [g]roup and pause the group.

`pueue kill -g {*{*group name}}`

- kill [a]ll tasks across all groups and pause all groups

`pueue kill -a`
