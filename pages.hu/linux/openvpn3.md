# openvpn3

> OpenVPN 3 Linux kliens. További információ: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- Új VPN-munkamenet indítása:

`openvpn3 session-start --config {{path/to/config.conf}}`

- Létrehozott munkamenetek listája:

`openvpn3 sessions-list`

- Az adott konfigurációval indított, jelenleg létrehozott munkamenet megszakítása:

`openvpn3 session-manage --config {{path/to/config.conf}} --disconnect`

- VPN-konfiguráció importálása:

`openvpn3 config-import --config {{path/to/config.conf}}`

- Importált konfigurációk listázása:

`openvpn3 configs-list`
