# ip neighbour

> Subcomando de gestión de tablas IP de vecinos/ARP.
> Más información: <https://manned.org/ip-neighbour.8>.

- Muestra las entradas de la tabla de vecinos/ARP:

`ip {{[n|neighbour]}}`

- Elimina entradas en la tabla de vecinos del dispositivo `eth0`:

`sudo ip {{[n|neighbour]}} {{[f|flush]}} dev {{eth0}}`

- Realiza una búsqueda de vecinos y devuelve una entrada de vecinos:

`ip {{[n|neighbour]}} {{[g|get]}} {{lookup_ip}} dev {{eth0}}`

- Agrega o elimina una entrada ARP a los vecinos IP de `eth0`:

`sudo ip {{[n|neighbour]}} {{add|delete}} {{dirección_ip}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- Cambia o reemplaza una entrada ARP para la dirección IP vecina a `eth0`:

`sudo ip {{[n|neighbour]}} {{change|replace}} {{dirección_ip}} lladdr {{nueva_mac_address}} dev {{eth0}}`
