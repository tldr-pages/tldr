# sockstat

> Toon open Internet- of UNIX-domeinsockets.
> Let op: dit programma is hergeschreven voor NetBSD 3.0 van FreeBSD's `sockstat`.
> Zie ook: `netstat`.
> Meer informatie: <https://man.netbsd.org/sockstat.1>.

- Toon informatie voor IPv4- en IPv6-sockets voor zowel luister- als verbonden sockets:

`sockstat`

- Toon informatie voor IPv[4]/IPv[6] sockets die [l]uisteren op specifieke [p]oorten met een specifiek [P]rotocol:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- Toon ook [c]onnected sockets en [u]nix-sockets:

`sockstat -cu`

- Toon alleen [n]umerieke output, zonder symbolische namen voor adressen en poorten te resolven:

`sockstat -n`

- Toon alleen sockets van de opgegeven adres[f]amilie:

`sockstat -f {{inet|inet6|local|unix}}`
