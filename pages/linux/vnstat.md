# vnstat

> A console-based network traffic monitor.

- Display traffic summary for all interfaces:

`vnstat`

- Display traffic summary for eth0:

`vnstat -i eth0`

- Display live stats for eth0:

`vnstat -l -i eth0`

- Show traffic statistics on a hourly basis for the last 24 hours using a bar graph:

`vnstat -hg`

- Measure and show average traffic for 30 seconds:

`vnstat -tr 30`
