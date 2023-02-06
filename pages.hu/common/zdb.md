# zdb

> ZFS debugger. További információ: <https://manned.org/zdb>.

- Az összes csatlakoztatott ZFS zpool részletes konfigurációjának megjelenítése:

`zdb`

- Egy adott ZFS-pool részletes konfigurációjának megjelenítése:

`zdb -C {{poolname}}`

- Statisztikák megjelenítése a blokkok számáról, méretéről és deduplikációjáról:

`zdb -b {{poolname}}`
