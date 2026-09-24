# mtr

> Matt's Traceroute: herramienta que combina traceroute y ping.
> Vea también: `traceroute`, `ping`.
> Más información: <https://manned.org/mtr>.

- Realiza un traceroute a un host y envía pings de forma continua a todos los saltos intermedios:

`mtr {{example.com}}`

- Desactiva la resolución de direcciones IP y nombres de host:

`mtr {{[-n|--no-dns]}} {{example.com}}`

- Genera un informe tras enviar 10 pings a cada salto:

`mtr {{[-w|--report-wide]}} {{example.com}}`

- Fuerza IPv4 o IPv6:

`mtr -4 {{example.com}}`

- Espera un tiempo determinado (en segundos) antes de enviar otro paquete al mismo salto:

`mtr {{[-i|--interval]}} {{10}} {{example.com}}`

- Muestra el número de sistema autónomo (ASN) de cada salto:

`mtr {{[-z|--aslookup]}} {{example.com}}`

- Muestra tanto la dirección IP como el nombre DNS inverso:

`mtr {{[-b|--show-ips]}} {{example.com}}`
