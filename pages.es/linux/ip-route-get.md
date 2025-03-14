# ip route get

> Obtiene una única ruta a un destino e imprime su contenido exactamente como el kernel lo ve.
> Más información: <https://manned.org/ip-route>.

- Imprime ruta a un destino:

`ip {{[r|route]}} {{[g|get]}} {{1.1.1.1}}`

- Imprime la ruta a un destino desde una dirección de origen específica:

`ip {{[r|route]}} {{[g|get]}} {{destino}} from {{origen}}`

- Imprime la ruta a un destino para los paquetes que llegan a una interfaz específica:

`ip {{[r|route]}} {{[g|get]}} {{destino}} iif {{eth0}}`

- Imprime la ruta a un destino forzando la salida a través de una interfaz específica:

`ip {{[r|route]}} {{[g|get]}} {{destino}} oif {{eth1}}`

- Imprime la ruta a un destino con un tipo específico de servicio (ToS):

`ip {{[r|route]}} {{[g|get]}} {{destino}} tos {{0x10}}`

- Imprime la ruta a un destino utilizando una instancia VRF específica (Virtual Routing and Forwarding - Enrutamiento y Reenvío Virtual):

`ip {{[r|route]}} {{[g|get]}} {{destino}} vrf {{myvrf}}`
