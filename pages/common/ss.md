# ss

> Display socket statistics.
> A modern replacement for netstat.
> More information: <https://man7.org/linux/man-pages/man8/ss.8.html>.

- Display all TCP sockets:

`ss -t`

- Display all listening sockets:

`ss -l`

- Display all TCP sockets with process names:

`ss -tp`

- Display listening TCP and UDP sockets with numeric addresses:

`ss -tuln`

- Display only IPv4 sockets:

`ss -4`

- Display only IPv6 sockets:

`ss -6`

- Display sockets using a specific port:

`ss -at '( dport = :{{port}} or sport = :{{port}} )'`

- Display summary statistics:

`ss -s`
