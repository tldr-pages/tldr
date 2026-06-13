# nmcli connection

> Beheer verbindingen met NetworkManager.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#connection>.

- Toon alle NetworkManager connecties (toont naam, UUID, type en apparaat):

`nmcli {{[c|connection]}}`

- Activeer een connectie:

`nmcli {{[c|connection]}} {{[u|up]}} {{uuid}}`

- Deactiveer een connectie:

`nmcli {{[c|connection]}} {{[d|down]}} {{uuid}}`

- Maak een automatisch geconfigueeerde dual stack connectie:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{interface_naam}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Maak een statische IPv6-only connectie:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{interface_naam}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Maak een statische IPv4-only connectie:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{interface_naam}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- Maak een VPN connectie via OpenVPN vanuit een OVPN bestand:

`nmcli {{[c|connection]}} {{[i|import]}} type {{openvpn}} file {{pad/naar/vpn_config.ovpn}}`
