# traceroute

> Muestra el seguimiento de la ruta de los paquetes hasta un host de red.
> Vea también: `mtr`.
> Más información: <https://manned.org/traceroute>.

- Traceroute a un host:

`traceroute {{example.com}}`

- Desactiva la asignación de direcciones IP y nombres de host:

`traceroute -n {{example.com}}`

- Especifica el tiempo de espera en segundos para la respuesta:

`traceroute {{[-w|--wait]}} {{0.5}} {{example.com}}`

- Especifica el número de consultas por salto:

`traceroute {{[-q|--queries]}} {{5}} {{example.com}}`

- Especifica el tamaño en bytes del paquete de sondeo:

`traceroute {{example.com}} {{42}}`

- Determina la MTU hasta el destino:

`traceroute --mtu {{example.com}}`

- Utiliza ICMP en lugar de UDP para el traceroute:

`traceroute {{[-I|--icmp]}} {{example.com}}`
