# prlimit

> Get or set process resource soft and hard limits.
> Given a process ID and one or more resources, prlimit tries to retrieve and/or modify the limits.
> More information: <https://askubuntu.com/questions/1367612/how-can-i-limit-the-cpu-and-ram-usage-for-a-process>.

- Display limit values for all current resources for the current process:

`prlimit`

- Display limit values for all current resources:

`prlimit --pid {{pid number}}`

- Run a command with a custom number of open files limit:

`prlimit --nofile={{number of open files}} {{command}}`
