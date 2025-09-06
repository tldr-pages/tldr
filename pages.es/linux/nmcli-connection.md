# nmcli connection

> Gestiona conexiones con NetworkManager.
> Este subcomando puede invocarse también con `nmcli c`.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Lista todas las conexiones NetworkManager (muestra nombre, UUID, tipo y dispositivo):

`nmcli connection`

- Activa una conexión:

`nmcli connection up uuid {{uuid}}`

- Desactiva una conexión:

`nmcli connection down uuid {{uuid}}`

- Crea una conexión de doble pila autoconfigurada:

`nmcli connection add ifname {{nombre_de_la_interfaz}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Crea una conexión estática exclusivamente IPv6:

`nmcli connection add ifname {{nombre_de_la_interfaz}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Crea una conexión estática exclusivamente IPv4:

`nmcli connection add ifname {{nombre_de_la_interfaz}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- Crea una conexión VPN usando OpenVPN desde un archivo OVPN:

`nmcli connection import type {{openvpn}} file {{ruta/a/configuración_vpn.ovpn}}`
