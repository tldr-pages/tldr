# ip address

> Subcomando de manejo de direcciones IP.
> Más información: <https://manned.org/ip-address>.

- Lista las interfaces de red y sus direcciones IP asociadas:

`ip address`

- Filtra mostrando solo las interfaces de red activas:

`ip address show up`

- Muestra información sobre una interfaz de red específica:

`ip address show dev {{eth0}}`

- Añade una dirección IP a una interfaz de red:

`ip address add {{dirección_ip}} dev {{eth0}}`

- Elimina una dirección IP de una interfaz de red:

`ip address delete {{dirección_ip}} dev {{eth0}}`

- Elimina todas las direcciones IP en un alcance dado de una interfaz de red:

`ip address flush dev {{eth0}} scope {{global|host|link}}`
