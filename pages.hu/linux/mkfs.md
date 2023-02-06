# mkfs

> Linux fájlrendszer létrehozása egy merevlemez partícióra. Ez a parancs elavult a fájlrendszer-specifikus mkfs javára. utils. További információ: <https://manned.org/mkfs>.

- Linux ext2 fájlrendszer létrehozása egy partícióra:

`mkfs {{path/to/partition}}`

- Egy megadott típusú fájlrendszer létrehozása:

`mkfs -t {{ext4}} {{path/to/partition}}`

- Egy megadott típusú fájlrendszer létrehozása és a rossz blokkok ellenőrzése:

`mkfs -c -t {{ntfs}} {{path/to/partition}}`
