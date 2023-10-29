# systemd-cgtop

> Show the top control groups of the local Linux control group hierarchy, ordered by their CPU, memory, or disk I/O load.
> See also: `top`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-cgtop.html>.

- Start an interactive view:

`systemd-cgtop`

- Change the sort order:

`systemd-cgtop --order={{cpu|memory|path|tasks|io}}`

- Show the CPU usage by time instead of percentage:

`systemd-cgtop --cpu=percentage`

- Change the update interval in seconds (or one of these time units: `ms`, `us`, `min`):

`systemd-cgtop --delay={{interval}}`

- Only count userspace processes (without kernel threads):

`systemd-cgtop -P`
