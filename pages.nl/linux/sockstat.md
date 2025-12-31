# sockstat

> Toon open Internet- of UNIX-domeinsockets.
> Zie ook: `netstat`.
> Meer informatie: <https://manned.org/sockstat>.

- Toon informatie voor IPv4- en IPv6-sockets voor zowel luister- als verbonden sockets:

`sockstat`

- Toon informatie voor IPv[4]/IPv[6] sockets die [l]uisteren op specifieke [p]oorten met een specifiek p[R]otocol:

`sockstat -{{4|6}} -l -R {{tcp|udp|sctp|divert}} -p {{poort1,poort2...}}`

- Toon ook [c]onnected sockets en [u]nix-sockets:

`sockstat -cu`

- Toon alleen sockets van het opgegeven `pid` of proces:

`sockstat -P {{pid|proces}}`

- Toon alleen sockets van de opgegeven `uid` of gebruiker:

`sockstat -U {{uid|gebruiker}}`

- Toon alleen sockets van de opgegeven `gid` of groep:

`sockstat -G {{gid|groep}}`
