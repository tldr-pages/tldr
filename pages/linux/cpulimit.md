# cpulimit

> A tool to throttle the CPU usage of other processes.
> More information: <https://manned.org/cpulimit>.

- Limit an existing process with PID 1234 to only use 25% of the CPU:

`cpulimit {{[-p|--pid]}} {{1234}} {{[-l|--limit]}} {{25%}}`

- Limit an existing program by its executable name:

`cpulimit {{[-e|--exe]}} {{program}} {{[-l|--limit]}} {{25}}`

- Launch a given program and limit it to only use 50% of the CPU:

`cpulimit {{[-l|--limit]}} {{50}} -- {{program argument1 argument2 ...}}`

- Launch a program, limit its CPU usage to 50% and run cpulimit in the background:

`cpulimit {{[-l|--limit]}} {{50}} {{[-b|--background]}} -- {{program}}`

- Kill its process if the program's CPU usage goes over 50%:

`cpulimit {{[-l|--limit]}} 50 {{[-k|--kill]}} -- {{program}}`

- Throttle both it and its child processes so that none go about 25% CPU:

`cpulimit {{[-l|--limit]}} {{25}} {{[-m|--monitor-forks]}} -- {{program}}`
