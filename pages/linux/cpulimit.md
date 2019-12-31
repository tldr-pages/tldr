# cpulimit

> A tool to throttle the CPU usage of other processes.
> More information: <http://cpulimit.sourceforge.net/>.

- Limit an existing process with PID 1234 to only use 25% of the CPU:

`cpulimit --pid {{1234}} --limit {{25%}}`

- Limit an existing program by its executable name:

`cpulimit --exe {{program}} --limit {{25}}`

- Launch a given program and limit it to only use 50% of the CPU:

`cpulimit --limit {{50}} -- {{program arg1 arg2 ...}}`

- Launch a program, limit its CPU usage to 50% and run cpulimit in the background:

`cpulimit --limit {{50}} --background -- {{program}}`

- Kill its process if the program's CPU usage goes over 50%:

`cpulimit --limit 50 --kill -- {{program}}`

- Throttle both it and its child processes so that none go about 25% CPU:

`cpulimit --limit {{25}} --monitor-forks -- {{program}}`
