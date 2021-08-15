# ionice

> Get or set program I/O scheduling class and priority.
> Scheduling classes: 1 (realtime), 2 (best-effort), 3 (idle).
> Priority levels: 0 (the highest) - 7 (the lowest).
> More information: <https://manned.org/ionice>.

- Set I/O scheduling class of a running process:

`ionice -c {{scheduling_class}} -p {{pid}}`

- Run a command with custom I/O scheduling class and priority:

`ionice -c {{scheduling_class}} -n {{priority}} {{command}}`

- Print the I/O scheduling class and priority of a running process:

`ionice -p {{pid}}`
