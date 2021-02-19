# pueue start

> Resume operation of specific tasks or groups of tasks.
> see also: pueue pause --help

- resume all tasks in default group

`pueue start`

- resume a specific task

`pueue start {{task ID}}`

- resume multiple tasks at once

`pueue start {{first task ID}} {{second task ID}} ...`

- resume [a]ll tasks and start their [c]hildren

`pueue start -ac`

- resume all tasks in a specific group 

`pueue start group {{group name}}`
