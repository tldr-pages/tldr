# cpulimit

> A tool to throttle the CPU usage of other processes.
> Homepage: <http://limitcpu.sourceforge.net/>.

- Limit an existing process with PID 1234 to only use 25% of the CPU:

`cpulimit -p {{1234}} -l {{25%}}`

- Limit an existing program by its executable name instead of PID number:

`cpulimit -e {{program}} -l {{25}}`

- Launch a given program and limit it to only use 50% of the CPU:

`cpulimit -l {{50}} {{program}}`

- Launch a program, limit its CPU usage to 50% and run cpulimit in the background:

`cpulimit -l {{50}} -b {{program}}`

- Launch a program and kill its process if the program's CPU usage goes over 50%:

`cpulimit -l 50 -k {{program}}`

- Launch a program and throttle both it and its child processes so that none go about 25% CPU:

`cpulimit -l {{25}} -m {{program}}`
