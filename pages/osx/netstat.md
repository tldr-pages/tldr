# netstat

> Display network-related information such as open connections, open socket ports, etc.
> More information: <https://keith.github.io/xcode-man-pages/netstat.1.html>.

- Display the PID and program name listening on a specific protocol:

`netstat -p {{protocol}}`

- Print the routing table and do not resolve IP addresses to hostnames:

`netstat -nr`

- Print the routing table of IPv4 addresses:

`netstat -nr -f inet`
