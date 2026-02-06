# dhcpcd

> Cliente DHCP.
> Más información: <https://roy.marples.name/projects/dhcpcd>.

- Libera todas las direcciones:

`sudo dhcpcd {{[-k|--release]}}`

- Solicita nuevas direcciones al servidor DHCP:

`sudo dhcpcd {{[-n|--rebind]}}`

- Mostrar el último arrendamiento obtenido para una interfaz y salir:

`sudo dhcpcd {{[-U|--dumplease]}} {{nombre_interface}}`
