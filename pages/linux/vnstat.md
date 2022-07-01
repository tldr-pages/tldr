# vnstat

> A console-based network traffic monitor.
> More information: <https://manned.org/vnstat>.

- Display traffic summary for all interfaces:

`vnstat`

- Display traffic summary for a specific network interface:

`vnstat -i {{eth0}}`

- Display live stats for a specific network interface:

`vnstat -l -i {{eth0}}`

- Show traffic statistics on an hourly basis for the last 24 hours using a bar graph:

`vnstat -hg`

- Measure and show average traffic for 30 seconds:

`vnstat -tr {{30}}`
