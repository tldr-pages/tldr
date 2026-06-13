# dhcpcd

> Cliente DHCP.
> Más información: <https://roy.marples.name/projects/dhcpcd>.

- Libera todas las direcciones:

`sudo dhcpcd {{[-k|--release]}}`

- Solicita nuevas direcciones al servidor DHCP:

`sudo dhcpcd {{[-n|--rebind]}}`

- Muestra el último arrendamiento obtenido para una interfaz y sale:

`sudo dhcpcd {{[-U|--dumplease]}} {{nombre_interface}}`
