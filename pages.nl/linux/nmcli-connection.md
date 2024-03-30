# nmcli connection

> Beheer verbindingen met NetworkManager.
> Dit subcommando kan ook aangeroepen worden met `nmcli c`.
> Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon alle NetworkManager connecties (toont naam, UUID, type en apparaat):

`nmcli connection`

- Activeer een connectie:

`nmcli connection up uuid {{uuid}}`

- Deactiveer een connectie:

`nmcli connection down uuid {{uuid}}`

- Maak een automatisch geconfigueeerde dual stack connectie:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Maak een statische IPv6-only connectie:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Maak een statische IPv4-only connectie:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- Maak een VPN connectie via OpenVPN vanuit een OVPN bestand:

`nmcli connection import type {{openvpn}} file {{pad/naar/vpn_config.ovpn}}`
