# quotacheck

> A fájlrendszer lemezhasználatának vizsgálata; kvótafájlok létrehozása, ellenőrzése és javítása. A legjobb, ha a kvótaellenőrzést kikapcsolt kvóták mellett futtatjuk, hogy elkerüljük a kvótafájlok károsodását vagy elvesztését. További információ: <https://manned.org/quotacheck>.

- Ellenőrizze a kvótákat az összes csatlakoztatott, nem NFS fájlrendszeren:

`sudo quotacheck --all`

- Kényszerítse az ellenőrzést akkor is, ha a kvóták engedélyezve vannak (ez a kvótafájlok sérülését vagy elvesztését okozhatja):

`sudo quotacheck --force {{mountpoint}}`

- A kvóták ellenőrzése egy adott fájlrendszeren hibakeresési módban:

`sudo quotacheck --debug {{mountpoint}}`

- A kvóták ellenőrzése egy adott fájlrendszeren, az előrehaladás megjelenítésével:

`sudo quotacheck --verbose {{mountpoint}}`

- Felhasználói kvóták ellenőrzése:

`sudo quotacheck --user {{user}} {{mountpoint}}`

- Csoportos kvóták ellenőrzése:

`sudo quotacheck --group {{group}} {{mountpoint}}`
