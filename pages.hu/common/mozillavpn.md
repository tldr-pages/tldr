# mozillavpn

> Virtuális magánhálózat a Firefox készítőitől. További információ: <https://github.com/mozilla-mobile/mozilla-vpn-client/wiki/Command-line-interface>.

- Bejelentkezés egy interaktív kéréssel:

`mozillavpn login`

- Csatlakozás a Mozilla VPN-hez:

`mozillavpn activate`

- A kapcsolat állapotának megjelenítése:

`mozillavpn status`

- Az elérhető szerverek listája:

`mozillavpn servers`

- Egy adott kiszolgáló kiválasztása:

`mozillavpn select {{server_name}}`

- A Mozilla VPN-hez való csatlakozás megszakítása:

`mozillavpn deactivate`

- Kijelentkezés:

`mozillavpn logout`

- Súgó megjelenítése egy alparancshoz:

`mozillavpn {{subcommand}} --help`
