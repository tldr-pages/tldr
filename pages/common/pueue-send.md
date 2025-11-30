# pueue send

> Send input to a task.
> More information: <https://github.com/Nukesor/pueue#how-to-use-it>.

- Send input to a running command:

`pueue send {{task_id}} "{{input}}"`

- Send confirmation to a task expecting y/N (e.g. APT, cp):

`pueue send {{task_id}} {{y}}`
