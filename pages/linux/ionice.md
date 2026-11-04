# ionice

> Get or set program I/O scheduling class and priority.
> Scheduling classes: 1 (realtime), 2 (best-effort), 3 (idle).
> Priority levels: 0 (the highest) - 7 (the lowest).
> More information: <https://manned.org/ionice>.

- Run a command with the given scheduling class and priority:

`ionice {{[-c|--class]}} {{scheduling_class}} {{[-n|--classdata]}} {{priority}} {{command}}`

- Set I/O scheduling class of a running process with a specific [p]id, [P]gid, or [u]id:

`ionice {{[-c|--class]}} {{scheduling_class}} -{{p|P|u}} {{id}}`

- Set the priority of a running process, ignoring failure to do so (this can happen due to insufficient privileges or an old kernel version):

`ionice {{[-t|--ignore]}} {{[-n|--classdata]}} {{priority}} {{[-p|--pid]}} {{process_id}}`

- Print the I/O scheduling class and priority of a running process:

`ionice {{[-p|--pid]}} {{process_id}}`
