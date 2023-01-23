# cryfs

> Kriptográfiai fájlrendszer a felhő számára. További információ: <https://www.cryfs.org/>.

- Titkosított fájlrendszer csatlakoztatása. Az inicializáló varázsló az első végrehajtáskor elindul:

`cryfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Egy titkosított fájlrendszer leválasztása:

`cryfs-unmount {{path/to/mount_point}}`

- Automatikusan leválasztja a csatolást tíz perc inaktivitás után:

`cryfs --unmount-idle {{10}} {{path/to/cipher_dir}} {{path/to/mount_point}}`

- A támogatott kódok listájának megjelenítése:

`cryfs --show-ciphers`
