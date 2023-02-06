# btrfs rescue

> Próbálja meg helyreállítani a sérült btrfs fájlrendszert. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- A fájlrendszer metaadatfájának újjáépítése (nagyon lassú):

`sudo btrfs rescue chunk-recover {{path/to/partition}}`

- Az eszközmérettel kapcsolatos igazítási problémák javítása (pl. nem tudja csatlakoztatni a fájlrendszert szuper total byte eltérés esetén):

`sudo btrfs rescue fix-device-size {{path/to/partition}}`

- Megrongálódott szuperblokk helyreállítása helyes másolatokból (a fájlrendszer fájának gyökerének helyreállítása):

`sudo btrfs rescue super-recover {{path/to/partition}}`

- Megszakadt tranzakcióból való helyreállítás (a naplóvisszajátszási problémák javítása):

`sudo btrfs rescue zero-log {{path/to/partition}}`

- A `/dev/btrfs-control` vezérlőeszköz létrehozása, ha a `mknod` nincs telepítve:

`sudo btrfs rescue create-control-device`
