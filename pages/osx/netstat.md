# netstat

> Display network-related information such as open connections, open socket ports, etc.
> More information: <https://man.freebsd.org/cgi/man.cgi?netstat(1)>.

- Displays the PID and program name listening on the given protocol listen:

`netstat -p {{protocol}}`

- Print the routing table and do not resolve IP addresses to hostnames:

`netstat -nr`

- Print the routing table of IPv4 addresses:

`netstat -nr -f inet`
