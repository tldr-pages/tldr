# ping6

> Enviar paquetes ICMP ECHO_REQUEST ("pings") a hosts de la red usando direcciones IPv6.
>  Más información: <https://manned.org/ping6>.

- Enviar pings a un host:

`ping6 {{host}}`

- Enviar un número determinado de pings a un host:

`ping6 -c {{numero}} {{host}}`

- Enviar pings a un host especificando el intervalo de tiempo entre peticiones (por defecto un segundo):

`ping6 -i {{segundos}} {{host}}`

- Enviar pings a un host sin intentar resolver nombres simbólicos de direcciones:

`ping6 -n {{host}}`

- Enviar pings a un host y emitir un sonido cuando un paquete sea recibido (si la terminal lo soporta):

`ping6 -a {{host}}`
