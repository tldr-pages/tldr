# zpool

> ZFS-medencék kezelése. További információ: <https://manned.org/zpool>.

- Az összes ZFS zpool konfigurációjának és állapotának megjelenítése:

`zpool status`

- A ZFS-medence hibaellenőrzése (ellenőrzi MINDEN blokk ellenőrző összegét). Nagyon CPU- és lemezigényes:

`zpool scrub {{pool_name}}`

- Importálásra rendelkezésre álló zpoolok listázása:

`zpool import`

- Importáljon egy zpoolt:

`zpool import {{pool_name}}`

- Zpool exportálása (az összes fájlrendszer leválasztása):

`zpool export {{pool_name}}`

- Az összes pool-művelet előzményeinek megjelenítése:

`zpool history {{pool_name}}`

- Tükrözött pool létrehozása:

`zpool create {{pool_name}} mirror {{disk1}} {{disk2}} mirror {{disk3}} {{disk4}}`

- Cache (L2ARC) eszköz hozzáadása egy zpoolhoz:

`zpool add {{pool_name}} cache {{cache_disk}}`
