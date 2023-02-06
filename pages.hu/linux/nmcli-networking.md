# nmcli networking

> A NetworkManager hálózati állapotának kezelése. Ez az alparancs a `nmcli n` címmel is meghívható. További információ: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- A NetworkManager hálózati állapotának megjelenítése:

`nmcli networking`

- A hálózat és a NetworkManager által kezelt összes interfész engedélyezése vagy letiltása:

`nmcli networking {{on|off}}`

- Az utolsó ismert kapcsolódási állapot megjelenítése:

`nmcli networking connectivity`

- Az aktuális kapcsolódási állapot megjelenítése:

`nmcli networking connectivity check`
