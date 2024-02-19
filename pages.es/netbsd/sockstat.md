# sockstat

> Lista sockets abiertos de Internet o dominios UNIX.
> Nota: este programa es una reescritura para NetBSD 3.0 de `sockstat` de FreeBSD.
> Vea también: `netstat`.
> Más información: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Muestra información de sockets IPv4, IPv6 y Unix que estén escuchando y conectados:

`sockstat`

- Muestra información para sockets IPv[4]/IPv[6] escuchando ([l]istening) sobre [p]uertos específicos usando un [P]rotocolo específico:

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{puerto1,puerto2...}}`

- También muestra sockets [c]onectados, mostrando sockets [u]nix:

`sockstat -cu`

- Solo muestra salida [n]umérica, sin resolver nombres simbólicos para direcciones y puertos:

`sockstat -n`

- Lista sockets de una [f]amilia de direcciones específica:

`sockstat -f {{inet|inet6|local|unix}}`
