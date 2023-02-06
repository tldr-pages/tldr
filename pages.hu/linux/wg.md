# wg

> A WireGuard-interfészek konfigurációjának kezelése. További információ: <https://www.wireguard.com/quickstart/>.

- A jelenleg aktív interfészek állapotának ellenőrzése:

`wg`

- Új privát kulcs generálása:

`wg genkey`

- Nyilvános kulcs generálása egy magánkulcsból:

`wg pubkey < {{path/to/private_key}} > {{path/to/public_key}}`

- Nyilvános és magánkulcs generálása:

`wg genkey | tee {{path/to/private_key}} | wg pubkey > {{path/to/public_key}}`

- A Wireguard-interfész aktuális konfigurációjának megjelenítése:

`wg showconf {{wg0}}`
