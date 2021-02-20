# pueue restart

> Restart tasks.
> More information: <https://github.com/Nukesor/pueue>.

- Restart a specific task:

`pueue restart {{task ID}}`

- Restart multiple tasks at once, and start them immediately (do not enqueue):

`pueue restart --start-immediately {{first task ID}} {{second task ID}} ...`

- Restart a specific task from a different path:

`pueue restart -p {{task ID}}`

- Edit a command before restarting:

`pueue restart -e {{task ID}}`

- Restart a task [i]n-place (without enqueuing as a separate task):

`pueue restart -i {{task ID}}`

- Restart [a]ll failed tasks and [s]tash them:

`pueue restart -as`
