# zfs

> ZFS fájlrendszerek kezelése. További információ: <https://manned.org/zfs>.

- Az összes elérhető zfs fájlrendszer listázása:

`zfs list`

- Új ZFS fájlrendszer létrehozása:

`zfs create {{pool_name/filesystem_name}}`

- ZFS fájlrendszer törlése:

`zfs destroy {{pool_name/filesystem_name}}`

- Pillanatfelvétel készítése egy ZFS fájlrendszerről:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Tömörítés engedélyezése egy fájlrendszeren:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Csatlakozási pont módosítása egy fájlrendszerhez:

`zfs set mountpoint={{/my/mount/path}} {{pool_name/filesystem_name}}`
