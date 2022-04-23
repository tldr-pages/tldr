# sar

> Monitor performance of various Linux subsystems.
> More information: <https://manned.org/sar>.

- Report I/O and transfer rate issued to physical devices, one per second (press CTRL+C to quit):

`sar -b {{1}}`

- Report a total of 10 network device statistics, one per 2 seconds:

`sar -n DEV {{2}} {{10}}`

- Report CPU utilization, one per 2 seconds:

`sar -u ALL {{2}}`

- Report a total of 20 memory utilization statistics, one per second:

`sar -r ALL {{1}} {{20}}`

- Report the run queue length and load averages, one per second:

`sar -q {{1}}`

- Report paging statistics, one per 5 seconds:

`sar -B {{5}}`
