# netstat

> Display active TCP connections, ports on which the computer is listening, network adapter statistics, the IP routing table, IPv4 statistics and IPv6 statistics.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- Display active TCP connections:

`netstat`

- Display all active TCP connections and the TCP and UDP ports on which the computer is listening:

`netstat -a`

- Display network adapter statistics, such as the number of bytes and packets sent and received:

`netstat -e`

- Display active TCP connections and express addresses and port numbers numerically:

`netstat -n`

- Display active TCP connections and include the process ID (PID) for each connection:

`netstat -o`

- Display the contents of the IP routing table:

`netstat -r`

- Display statistics by protocol:

`netstat -s`

- Display a list of currently open ports and related IP addresses:

`netstat -an`
