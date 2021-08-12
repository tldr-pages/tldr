# nmcli connection

> Gestionarea conexiunilor cu NetworkManager.
> Mai multe informaţii: <https://man.archlinux.org/man/nmcli.1>

- Listați toate conexiunile NetworkManager (afișează numele, uuid, tipul și dispozitivul):

`nmcli connection`

- Activați o conexiune specificând un uid:

`nmcli connection up uuid {{uuid}}`

- Dezactivează o conexiune:

`nmcli connection down uuid {{uuid}}`

- Creați o conexiune duală configurată automat:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Creați o conexiune statică numai IPv6:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Creați o conexiune statică numai IPv4:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- Creați o conexiune VPN utilizând OpenVPN dintr-un fișier OVPN:

`nmcli connection import type {{openvpn}} file {{path/to/vpn_config.ovpn}}`
