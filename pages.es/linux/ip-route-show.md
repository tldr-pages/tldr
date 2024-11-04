# ip route show

> Subcomando para mostrar la gestión de tablas de enrutamiento IP.
> Más información: <https://manned.org/ip-route>.

- Muestra la tabla de enrutamiento:

`ip route show`

- Muestra la tabla principal de enrutamiento (igual al primer ejemplo):

`ip route show {{main|254}}`

- Muestra la tabla de enrutamiento local:

`ip route show table {{local|255}}`

- Muestra todas las tablas de enrutamiento:

`ip route show table {{all|unspec|0}}`

- Lista solamente las rutas desde un dispositivo dado:

`ip route show dev {{eth0}}`

- Lista las rutas dentro de un alcance determinado:

`ip route show scope link`

- Muestra el caché de enrutamiento:

`ip route show cache`

- Muestra solo rutas IPv6 o IPv4:

`ip {{-6|-4}} route show`
