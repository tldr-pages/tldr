# pidstat

> Show system resource usage, including CPU, memory, IO etc.

- Show CPU statistics at a 2 second interval for 10 times:

`pidstat {{2}} {{10}}`

- Show page faults and memory utilization:

`pidstat -r`

- Show input/output usage per process id:

`pidstat -d`

- Show information on a specific PID:

`pidstat -p {{PID}}`

- Show memory statistics for all processes whose command name include "fox" or "bird":

`pidstat -C "{{fox|bird}}" -r -p ALL`
