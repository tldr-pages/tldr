# ip route

> Subcomando de gestión de tablas de enrutamiento IP.
> Más información: <https://manned.org/ip-route>.

- Muestra la tabla de enrutamiento:

`ip route {{show|list}}`

- Agrega una ruta predeterminada usando reenvío de puerta de enlace (gateway):

`sudo ip route add default via {{ip_de_gateway}}`

- Añade una ruta predeterminada utilizando `eth0`:

`sudo ip route add default dev {{eth0}}`

- Añade una ruta estática:

`sudo ip route add {{ip_destino}} via {{ip_de_gateway}} dev {{eth0}}`

- Elimina una ruta estática:

`sudo ip route del {{ip_destino}} dev {{eth0}}`

- Cambia o reemplaza una ruta estática:

`sudo ip route {{change|replace}} {{ip_destino}} via {{ip_de_gateway}} dev {{eth0}}`

- Muestra qué ruta será utilizada por el kernel para llegar a una dirección IP:

`ip route get {{ip_destino}}`
