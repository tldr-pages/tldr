# swupd

> Csomagkezelő segédprogram Clear Linuxhoz. További információ: <https://docs.01.org/clearlinux/latest/guides/clear/swupd.html>.

- Frissítés a legújabb verzióra:

`sudo swupd update`

- Megjeleníti az aktuális verziót, és ellenőrzi, hogy létezik-e újabb verzió:

`swupd check-update`

- Telepített csomagok listája:

`swupd bundle-list`

- Keresse meg azt a csomagot, amelyben a kívánt csomag létezik:

`swupd search -b {{package}}`

- Új csomag telepítése:

`sudo swupd bundle-add {{bundle}}`

- Egy csomag eltávolítása:

`sudo swupd bundle-remove {{bundle}}`

- Törött vagy hiányzó fájlok javítása:

`sudo swupd verify`
