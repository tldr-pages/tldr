# pueue group

> Display, add or remove groups.
> More information: <https://github.com/Nukesor/pueue>.

- Show all groups with their statuses and number of parallel jobs:

`pueue group`

- Add a custom group:

`pueue group --add "{{group_name}}"`

- Remove a group and move its tasks to the default group:

`pueue group --remove "{{group_name}}"`
