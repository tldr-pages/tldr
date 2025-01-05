# ip

> Muestra/manipula enrutamientos, dispositivos, políticas de enrutamiento y túneles.
> Algunos subcomandados como `address` tienen su propia documentación de uso.
> Más información: <https://www.manned.org/ip.8>.

- Lista las interfaces con información detallada:

`ip address`

- Lista las interfaces con información breve de capa de red:

`ip -brief address`

- Lista las interfaces con información breve dada una capa de enlace:

`ip -brief link`

- Muestra la tabla de enrutamiento:

`ip route`

- Muestra vecinos (tabla ARP):

`ip neighbour`

- Establece una interfaz arriba/abajo (up/down). Usa inglés:

`ip link set {{interfaz}} {{up|down}}`

- Agrega/borra una dirección IP de una interfaz:

`ip addr add/del {{ip}}/{{mask}} dev {{interfaz}}`

- Agrega una ruta predeterminada:

`ip route add default via {{ip}} dev {{interfaz}}`
