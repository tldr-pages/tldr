# cpuctl

> Control and inspect system CPUs from command line.
> At least one CPU in the system must always remain online.
> More information: <https://man.netbsd.org/cpuctl.8>.

- Display the current state and time of last state change for each CPU in the system:

`sudo cpuctl list`

- Set the specified CPUs offline:

`sudo cpuctl offline {{cpu_number1 cpu_number2 ...}}`

- Set the specified CPUs online:

`sudo cpuctl online {{cpu_number1 cpu_number2 ...}}`
