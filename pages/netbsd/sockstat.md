# sockstat

> List open Internet or UNIX domain sockets.
> Note: this program is a rewrite for NetBSD 3.0 from FreeBSD's `sockstat`.
> See also: `netstat`.
> More information: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Show information for IPv4, IPv6 and Unix sockets for both listening and connected sockets:

`sockstat`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific [P]rotocol:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- Also show [c]onnected sockets, showing [u]nix sockets:

`sockstat -cu`

- Only show [n]umeric output, without resolving symbolic names for addresses and ports:

`sockstat -n`

- Only list sockets of the specified address [f]amily:

`sockstat -f {{inet|inet6|local|unix}}`
