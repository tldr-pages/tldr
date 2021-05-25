# pueue reset

> Kill everything and reset.
> More information: <https://github.com/Nukesor/pueue>.

- Kill all tasks and remove everything (logs, status, groups, task IDs):

`pueue reset`

- Kill all tasks, terminate their children, and reset everything:

`pueue reset --children`

- Reset without asking for confirmation:

`pueue reset --force`
