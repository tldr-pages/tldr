# pidstat

> Show system resource usage, including CPU, memory, IO etc.

- Show CPU statistics at two second intervals for 10 times:

`pidstat {{interval}} {{times}}`

- Show page faults and memory utilization:

`pidstat -r`

- Show io usage per process id:

`pidstat -d`

- Show specific PID:

`pidstat -p {{PID}}`

- Show memory statistics for all processes whose command name inclues string "fox" or "bird":

`pidstat -C "fox|bird" -r -p ALL`
