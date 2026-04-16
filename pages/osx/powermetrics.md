# powermetrics

> Gather and display CPU usage statistics, timer/interrupt frequencies, and macOS device power consumption.
> Note: this command requires root privileges.
> More information: <https://keith.github.io/xcode-man-pages/powermetrics.1.html>.

- Show power metrics for the system, sampling every 5 seconds (5000 ms) by default:

`sudo powermetrics`

- Sample power metrics at a specific interval (in milliseconds):

`sudo powermetrics --sample-rate {{interval_ms}}`

- Stop taking samples after a specific number of times:

`sudo powermetrics --sample-count {{count}}`

- Only show a specific group of power metrics:

`sudo powermetrics --samplers {{cpu_power|gpu_power|tasks|disk|network|thermal}}`

- Order the process list output by a specific metric (composite is the default):

`sudo powermetrics --order {{pid|wakeups|cputime|composite}}`

- Output the power metrics to a specified file:

`sudo powermetrics --output-file {{path/to/file.txt}}`
