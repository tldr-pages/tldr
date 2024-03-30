# prlimit

> Get or set process resource soft and hard limits.
> Given a process ID and one or more resources, prlimit tries to retrieve and/or modify the limits.
> More information: <https://manned.org/prlimit>.

- Display limit values for all current resources for the running parent process:

`prlimit`

- Display limit values for all current resources of a specified process:

`prlimit --pid {{pid_number}}`

- Run a command with a custom number of open files limit:

`prlimit --nofile={{10}} {{command}}`
