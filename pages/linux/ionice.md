# ionice

> Get or set program I/O scheduling class and priority.
> Scheduling classes: 1 (realtime), 2 (best-effort), 3 (idle).
> Priority levels: 0 (the highest) - 7 (the lowest).
> More information: <https://manned.org/ionice>.

- Run a command with the given scheduling class and priority:

`ionice {{[-c|--class]}} {{scheduling_class}} {{[-n|--classdata]}} {{priority}} {{command}}`

- Set I/O scheduling class of a running process with a specific [p]id, [P]gid or [u]id:

`ionice {{[-c|--class]}} {{scheduling_class}} -{{p|P|u}} {{id}}`

- Run a command with custom I/O scheduling class and priority:

`ionice {{[-c|--class]}} {{scheduling_class}} {{[-n|--classdata]}} {{priority}} {{command}}`

- Ignore failure to set the requested priority:

`ionice {{[-t|--ignore]}} {{[-n|--classdata]}} {{priority}} {{[-p|--pid]}} {{pid}}`

- Run the command even in case it was not possible to set the desired priority (this can happen due to insufficient privileges or an old kernel version):

`ionice {{[-t|--ignore]}} {{[-n|--classdata]}} {{priority}} {{[-p|--pid]}} {{pid}}`

- Print the I/O scheduling class and priority of a running process:

`ionice {{[-p|--pid]}} {{pid}}`
