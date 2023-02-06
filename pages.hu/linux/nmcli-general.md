# nmcli general

> A NetworkManager általános beállításainak kezelése. Ez az alparancs a `nmcli g` címmel is meghívható. További információ: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- A NetworkManager általános állapotának megjelenítése:

`nmcli general`

- Az aktuális eszköz állomásnevének megjelenítése:

`nmcli general hostname`

- Az aktuális eszköz állomásnevének módosítása:

`sudo nmcli general hostname {{new_hostname}}`

- A NetworkManager jogosultságainak megjelenítése:

`nmcli general permissions`

- Az aktuális naplózási szint és tartományok megjelenítése:

`nmcli general logging`

- Naplózási szint és/vagy tartományok beállítása (az összes elérhető tartományt lásd a `man NetworkManager.conf` oldalon):

`nmcli general logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domain_1,domain_2,...}}`
