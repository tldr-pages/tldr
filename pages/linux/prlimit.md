# prlimit

> Get or set process resource soft and hard limits.
> Given a process ID and one or more resources, prlimit tries to retrieve and/or modify the limits.
> More information: <https://man7.org/linux/man-pages/man1/prlimit.1.html>.

- Display limit values for all current resources for the current process:

`prlimit`

- Display limit values for all current resources of a specified process:

`prlimit --pid {{pid number}}`

- Run a command with a custom number of open files limit:

`prlimit --nofile={{10}} {{command}}`
