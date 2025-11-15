# iostat

> Report statistics for devices.
> More information: <https://ss64.com/mac/iostat.html>.

- Display snapshot device statistics (kilobytes per transfer, transfers per second, megabytes per second), CPU statistics (percentages of time spent in user mode, system mode, and idle mode), and system load averages (for the past 1, 5, and 15 min):

`iostat`

- Display only device statistics:

`iostat -d`

- Display incremental reports of CPU and disk statistics every 2 seconds:

`iostat 2`

- Display statistics for the first disk every second indefinitely:

`iostat -w 1 disk0`

- Display statistics for the second disk every 3 seconds, 10 times:

`iostat -w 3 -c 10 disk1`

- Display using old-style `iostat` display. Shows sectors transferred per second, transfers per second, average milliseconds per transaction, and CPU statistics + load averages from default-style display:

`iostat -o`

- Display total device statistics (KB/t: kilobytes per transfer as before, xfrs: total number of transfers, MB: total number of megabytes transferred):

`iostat -I`
