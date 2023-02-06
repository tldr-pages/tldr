# e2undo

> Az ext2/ext3/ext4 fájlrendszerek visszavonási naplóinak visszajátszása. Ezt arra lehet használni, hogy egy e2fsprogs program által végrehajtott sikertelen műveletet visszavonjon. További információ: <https://man7.org/linux/man-pages/man8/e2undo.8.html>.

- Egy adott undo fájlra vonatkozó információk megjelenítése:

`e2undo -h {{path/to/undo_file}} {{/dev/sdXN}}`

- Száraz futtatás végrehajtása és az újrajátszásra jelölt blokkok megjelenítése:

`e2undo -nv {{path/to/undo_file}} {{/dev/sdXN}}`

- Visszavonási művelet végrehajtása:

`e2undo {{path/to/undo_file}} {{/dev/sdXN}}`

- Visszavonási művelet végrehajtása és a szöveges információk megjelenítése:

`e2undo -v {{path/to/undo_file}} {{/dev/sdXN}}`

- A blokk régi tartalmának kiírása egy visszavonási fájlba, mielőtt felülírna egy fájlrendszerblokkot:

`e2undo -z {{path/to/file.e2undo}} {{path/to/undo_file}} {{/dev/sdXN}}`
