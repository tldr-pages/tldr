# ip address

> Subcomando de manejo de direcciones IP.
> Más información: <https://manned.org/ip-address>.

- Lista las interfaces de red y sus direcciones IP asociadas:

`ip {{[a|address]}}`

- Filtra mostrando solo las interfaces de red activas:

`ip {{[a|address]}} show up`

- Muestra información sobre una interfaz de red específica:

`ip {{[a|address]}} show dev {{eth0}}`

- Añade una dirección IP a una interfaz de red:

`ip {{[a|address]}} add {{dirección_ip}} dev {{eth0}}`

- Elimina una dirección IP de una interfaz de red:

`ip {{[a|address]}} delete {{dirección_ip}} dev {{eth0}}`

- Elimina todas las direcciones IP en un alcance dado de una interfaz de red:

`ip {{[a|address]}} flush dev {{eth0}} scope {{global|host|link}}`
