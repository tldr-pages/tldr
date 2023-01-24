# ping

> Enviar paquetes ICMP ECHO_REQUEST ("pings") a hosts de la red.
> Más información: <https://manned.org/ping>.

- Enviar pings a un host:

`ping {{host}}`

- Enviar un número determinado de pings a un host:

`ping -c {{numero}} {{host}}`

- Enviar pings a un host especificando el intervalo de tiempo entre peticiones (por defecto un segundo):

`ping -i {{segundos}} {{host}}`

- Enviar pings a un host sin intentar resolver nombres simbólicos de direcciones:

`ping -n {{host}}`

- Enviar pings a un host y emitir un sonido cuando un paquete sea recibido (si la terminal lo soporta):

`ping -a {{host}}`

- Mostrar también un mensaje si no se recibió respuesta tras enviar un ping:

`ping -O {{host}}`
