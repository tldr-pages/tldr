# pueue send

> Send input to a task.
> More information: <https://github.com/Nukesor/pueue>.

- Send input to a running command:

`pueue send {{task_id}} "{{input}}"`

- Send confirmation to a task expecting y/N (e.g. apt, cp):

`pueue send {{task_id}} {{y}}`
