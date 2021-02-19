# pueue restart

> Restart tasks.

- restart a specific task

`pueue restart {{task ID}}`

- restart multiple tasks at once, and start them immediately (do not enqueue)

`pueue restart --start-immediately {{first task ID}} {{second task ID}} ...`

- restart a specific task from a different path

`pueue restart -p {{task ID}}`

- edit a command before restarting.

`pueue restart -e {{task ID}}`

- restart a task [i]n-place (without enqueuing as a separate task)

`pueue restart -i {{task ID}}`

- restart [a]ll failed tasks and [s]tash them.

`pueue restart -as`
