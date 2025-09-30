# ip address

> Subcomando de manejo de direcciones IP.
> Más información: <https://manned.org/ip-address>.

- Lista las interfaces de red y sus direcciones IP asociadas:

`ip {{[a|address]}}`

- Filtra mostrando solo las interfaces de red activas:

`ip {{[a|address]}} {{[s|show]}} up`

- Muestra información sobre una interfaz de red específica:

`ip {{[a|address]}} {{[s|show]}} {{eth0}}`

- Añade una dirección IP a una interfaz de red:

`sudo ip {{[a|address]}} {{[a|add]}} {{dirección_ip}} dev {{eth0}}`

- Elimina una dirección IP de una interfaz de red:

`sudo ip {{[a|address]}} {{[d|delete]}} {{dirección_ip}} dev {{eth0}}`

- Elimina todas las direcciones IP en un alcance dado de una interfaz de red:

`sudo ip {{[a|address]}} {{[f|flush]}} {{eth0}} scope {{global|host|link}}`
