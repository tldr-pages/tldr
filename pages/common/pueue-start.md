# pueue start

> Resume operation of specific tasks or groups of tasks.
> See also: pueue pause --help.

- Resume all tasks in default group:

`pueue start`

- Resume a specific task:

`pueue start {{task ID}}`

- Resume multiple tasks at once:

`pueue start {{first task ID}} {{second task ID}} ...`

- Resume [a]ll tasks and start their [c]hildren:

`pueue start -ac`

- Resume all tasks in a specific group:

`pueue start group {{group name}}`
