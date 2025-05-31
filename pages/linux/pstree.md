# pstree

> A convenient tool to show running processes as a tree.
> More information: <https://manned.org/pstree>.

- Display a tree of all processes (rooted at init):

`pstree`

- Display a tree of processes with PIDs:

`pstree {{[-p|--show-pids]}}`

- Display all process trees rooted at processes owned by specified user:

`pstree {{user}}`

- Display command line arguments:

`pstree {{[-a|--arguments]}}`

- Display children of a specified process:

`pstree {{pid}}`

- Display parents of a specified process:

`pstree {{[-s|--show-parents]}} {{pid}}`
