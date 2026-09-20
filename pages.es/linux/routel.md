# routel

> Muestra las rutas IP en un formato legible para el usuario.
> Vea también: `ip route`, `route`.
> Más información: <https://manned.org/routel>.

- Muestra la tabla de enrutamiento predeterminada:

`routel`

- Muestra una tabla de enrutamiento específica:

`routel {{número_tabla|main|local|default}}`

- Muestra solo rutas IPv4:

`routel {{[-4|--family inet]}}`

- Muestra solo rutas IPv6:

`routel {{[-6|--family inet6]}}`
