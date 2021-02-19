# pueue group

> Display, add or remove groups.

- Show all groups with their status and number of parallel jobs:

`pueue group`

- Add custom group:

`pueue group -a syncing_jobs`

- Remove group and move its tasks to the default group:

`pueue group -r CPU_intensive`
