# tune2fs

> Az ext2, ext3 vagy ext4 fájlrendszer paramétereinek beállítása. Használható beágyazott fájlrendszereken. További információ: <https://manned.org/tune2fs>.

- Állítsa be a fájlrendszer ellenőrzése előtti maximális számlálási számot 2-re:

`tune2fs -c {{2}} {{/dev/sdXN}}`

- Állítsa be a fájlrendszer címkéjét MY_LABEL értékre:

`tune2fs -L {{'MY_LABEL'}} {{/dev/sdXN}}`

- Engedélyezze a selejtezést és a felhasználó által megadott kiterjesztett attribútumokat egy fájlrendszerhez:

`tune2fs -o {{discard,user_xattr}} {{/dev/sdXN}}`

- Naplózás engedélyezése egy fájlrendszerhez:

`tune2fs -o^{{nobarrier}} {{/dev/sdXN}}`
