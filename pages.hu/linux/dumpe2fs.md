# dumpe2fs

> Az ext2/ext3/ext4 fájlrendszerek szuperblokk és blokkcsoport információinak nyomtatása. A parancs futtatása előtt bontsa le a partíciót a `umount {{device}}` segítségével. További információ: <https://manned.org/dumpe2fs>.

- Az ext2, ext3 és ext4 fájlrendszerek információinak megjelenítése:

`dumpe2fs {{/dev/sdXN}}`

- A fájlrendszerben rosszként lefoglalt blokkok megjelenítése:

`dumpe2fs -b {{/dev/sdXN}}`

- Kényszerítse a fájlrendszerinformációk megjelenítését még a felismerhetetlen funkciójelzőkkel is:

`dumpe2fs -f {{/dev/sdXN}}`

- Csak a szuperblokkinformációk megjelenítése, a blokkcsoport leírójának részletes információi nem:

`dumpe2fs -h {{/dev/sdXN}}`

- A részletes csoportinformációs blokkszámok nyomtatása hexadecimális formátumban:

`dumpe2fs -x {{/dev/sdXN}}`
