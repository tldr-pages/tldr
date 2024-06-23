# iostat

> Report statistics for devices.
> More information: <https://ss64.com/mac/iostat.html>.

- Display snapshot device statistics (**k**ilo**b**ytes per **t**ransfer, **t**ransfers **p**er **s**econd, **m**ega**b**ytes per **s**econd), CPU statistics (percentages of time spent in **us**er mode, **sy**stem mode, and **id**le mode), and system load averages (for the past 1 minute, 5 minutes, and 15 minutes):

`iostat`

- Display statistics for the first disk every second ad infinitum:

`iostat -w 1 disk0`

- Display statistics for the second disk every three seconds, ten times:

`iostat -w 3 -c 10 disk1`

- Display using old-style iostat display. Shows **s**ectors transferred **p**er **s**econd, **t**ransfers **p**er **s**econd, average milliseconds per transaction, and CPU statistics + load averages from default-style display

`iostat -o`

- Display incremental reports of CPU and disk statistics every 2 seconds:

`iostat 2`

- Display only device statistics:

`iostat -d`

- Display total device statistics (**KB/t**: kilobytes per transfer as before, **xfrs**: total number of transfers, **MB**: total number of megabytes transferred)
