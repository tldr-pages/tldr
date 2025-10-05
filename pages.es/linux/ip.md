# ip

> Muestra/manipula enrutamientos, dispositivos, políticas de enrutamiento y túneles.
> Algunos subcomandados como `address` tienen su propia documentación de uso.
> Más información: <https://manned.org/ip.8>.

- Lista las interfaces con información detallada:

`ip {{[a|address]}}`

- Lista las interfaces con información breve de capa de red:

`ip {{[-br a|-brief address]}}`

- Lista las interfaces con información breve dada una capa de enlace:

`ip {{[-br l|-brief link]}}`

- Muestra la tabla de enrutamiento:

`ip {{[r|route]}}`

- Muestra vecinos (tabla ARP):

`ip {{[n|neighbour]}}`

- Establece una interfaz arriba/abajo (up/down). Usa inglés:

`sudo ip {{[l|link]}} {{[s|set]}} {{interfaz}} {{up|down}}`

- Agrega/borra una dirección IP de una interfaz:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{interfaz}}`

- Agrega una ruta predeterminada:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{interfaz}}`
