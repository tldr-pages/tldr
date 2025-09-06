# chrt

> Manipulate the real-time attributes of a process.
> More information: <https://manned.org/chrt>.

- Display attributes of a process:

`chrt {{[-p|--pid]}} {{PID}}`

- Display attributes of all threads of a process:

`chrt {{[-a|--all-tasks]}} {{[-p|--pid]}} {{PID}}`

- Display the min/max priority values that can be used with `chrt`:

`chrt {{[-m|--max]}}`

- Set the scheduling priority of a process:

`chrt {{[-p|--pid]}} {{priority}} {{PID}}`

- Set the scheduling policy of a process:

`chrt --{{deadline|idle|batch|rr|fifo|other}} {{[-p|--pid]}} {{priority}} {{PID}}`
