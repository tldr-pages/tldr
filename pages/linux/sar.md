# sar

> Monitor performance of various Linux subsystems.

- Report I/O and transfer rate issued to physical devices, every second (press CTRL+C to quit):

`sar -b {{1}}`

- Report a total of 10 network device statistics, one per 2 seconds:

`sar -n DEV {{2}} {{10}}`

- Report CPU utilization every 2 seconds (press CTRL+C to quit):

`sar -u ALL {{2}}`

- Report a total of 20 memory utilization statistics,  one per second:

`sar -r ALL {{1}} {{20}}`

- Report the run queue length and load averages:

`sar -q {{1}} {{1}}`

- Report paging statistics every 5 seconds (press CTRL+C to quit):

`sar -B {{1}}`
