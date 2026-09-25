# chrt

> Manipulate the real-time attributes of a process.
> More information: <https://manned.org/chrt>.

- Display attributes of a process:

`chrt {{[-p|--pid]}} {{process_id}}`

- Display attributes of all threads of a process:

`chrt {{[-a|--all-tasks]}} {{[-p|--pid]}} {{process_id}}`

- Display the min/max priority values that can be used with `chrt`:

`chrt {{[-m|--max]}}`

- Set the scheduling priority of a process:

`chrt {{[-p|--pid]}} {{priority}} {{process_id}}`

- Set the scheduling policy of a process:

`chrt --{{deadline|idle|batch|rr|fifo|other}} {{[-p|--pid]}} {{priority}} {{process_id}}`
