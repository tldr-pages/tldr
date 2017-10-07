# sar

> Monitor performance of various Linux subsystems.

- Report I/O and Transfer rate every 1 second:

`sar -b 1`

- Report 10 network statistics every 2 seconds for network devices:

`sar -n DEV 2 10`

- Report CPU utilization every 2 seconds:

`sar -u ALL 2`

- Report 20 memory utilization statistics every 1 second:

`sar -r 1 20`

- Report queue length and load averages:

`sar -q 1 1`

- Report paging statistics every 1 second:

`sar -B 1`
