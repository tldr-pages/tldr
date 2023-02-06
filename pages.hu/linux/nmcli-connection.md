# nmcli connection

> Kapcsolatkezelés a NetworkManagerrel. Ez az alparancs a `nmcli c` címmel is meghívható. További információ: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Az összes NetworkManager-kapcsolat listázása (megmutatja a nevet, az UUID-t, a típust és az eszközt):

`nmcli connection`

- Egy kapcsolat aktiválása az UUID megadásával:

`nmcli connection up uuid {{uuid}}`

- Kapcsolat deaktiválása:

`nmcli connection down uuid {{uuid}}`

- Automatikusan konfigurált dual stack kapcsolat létrehozása:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- Statikus, csak IPv6-os kapcsolat létrehozása:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- Statikus, csak IPv4 kapcsolat létrehozása:

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- VPN-kapcsolat létrehozása OpenVPN használatával egy OVPN-fájlból:

`nmcli connection import type {{openvpn}} file {{path/to/vpn_config.ovpn}}`
