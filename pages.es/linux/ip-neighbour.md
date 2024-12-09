# ip neighbour

> Subcomando de gestión de tablas IP de vecinos/ARP.
> Más información: <https://manned.org/ip-neighbour.8>.

- Muestra las entradas de la tabla de vecinos/ARP:

`ip neighbour`

- Elimina entradas en la tabla de vecinos del dispositivo `eth0`:

`sudo ip neighbour flush dev {{eth0}}`

- Realiza una búsqueda de vecinos y devuelve una entrada de vecinos:

`ip neighbour get {{lookup_ip}} dev {{eth0}}`

- Agrega o elimina una entrada ARP a los vecinos IP de `eth0`:

`sudo ip neighbour {{add|del}} {{dirección_ip}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- Cambia o reemplaza una entrada ARP para la dirección IP vecina a `eth0`:

`sudo ip neighbour {{change|replace}} {{dirección_ip}} lladdr {{nueva_mac_address}} dev {{eth0}}`
