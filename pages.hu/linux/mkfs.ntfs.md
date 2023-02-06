# mkfs.ntfs

> NTFS fájlrendszert hoz létre egy partíción belül. További információ: <https://manned.org/mkfs.ntfs>.

- NTFS fájlrendszer létrehozása az 1. partíción belül a b eszközön (`sdb1`):

`mkfs.ntfs {{/dev/sdb1}}`

- Létrehozza a fájlrendszert egy kötetcímkével:

`mkfs.ntfs -L {{volume_label}} {{/dev/sdb1}}`

- Speciális UUID-vel rendelkező fájlrendszer létrehozása:

`mkfs.ntfs -U {{UUID}} {{/dev/sdb1}}`
