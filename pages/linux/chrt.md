# chrt

> Manipulate the real-time attributes of a process.
> More information: <https://man7.org/linux/man-pages/man1/chrt.1.html>.

- Display attributes of a process:

`chrt --pid {{PID}}`

- Display attributes of all threads of a process:

`chrt --all-tasks --pid {{PID}}`

- Display the min/max priority values that can be used with `chrt`:

`chrt --max`

- Set the scheduling policy for a process:

`chrt --{{deadline|idle|batch|rr|fifo|other}} --pid {{priority}} {{PID}}`
