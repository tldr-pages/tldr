# sockstat

> List open Internet or UNIX domain sockets. Rewrite for NetBSD 3.0 from FreeBSD's `sockstat`.
> Some of the displayed informations: USER, COMMAND, PID, FD (file descriptor), PROTO (protocol).
> See also: `netstat`.
> More information: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Show information for IPv4, IPv6 and Unix sockets for both listening and connected sockets:

`sockstat`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific [P]rotocol:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- Also show [c]onnected sockets, showing [u]nix sockets:

`sockstat -cu`

- Only show [n]umeric output, not looking symbolic names for addresses and ports:

`sockstat -n`

- Only list sockets of the specified address family:

`sockstat -f {{inet|inet6|local|unix}}`
