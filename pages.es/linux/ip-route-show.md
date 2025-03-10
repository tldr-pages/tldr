# ip route show

> Subcomando para mostrar la gestión de tablas de enrutamiento IP.
> Más información: <https://manned.org/ip-route>.

- Muestra la tabla de enrutamiento:

`ip {{[r|route]}} show`

- Muestra la tabla principal de enrutamiento (igual al primer ejemplo):

`ip {{[r|route]}} show {{main|254}}`

- Muestra la tabla de enrutamiento local:

`ip {{[r|route]}} show table {{local|255}}`

- Muestra todas las tablas de enrutamiento:

`ip {{[r|route]}} show table {{all|unspec|0}}`

- Lista solamente las rutas desde un dispositivo dado:

`ip {{[r|route]}} show dev {{eth0}}`

- Lista las rutas dentro de un alcance determinado:

`ip {{[r|route]}} show scope link`

- Muestra el caché de enrutamiento:

`ip {{[r|route]}} show cache`

- Muestra solo rutas IPv6 o IPv4:

`ip {{-6|-4}} {{[r|route]}} show`
