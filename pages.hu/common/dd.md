# dd

> Fájlok átalakítása és másolása. További információ: <https://www.gnu.org/software/coreutils/dd>.

- Készítsen bootolható USB-meghajtót egy izohibrid fájlból (pl. `archlinux-xxx.iso`):

`dd if={{path/to/file.iso}} of=/dev/{{usb_drive}}`

- Klónozzon egy meghajtót egy másik meghajtóra 4 MiB-os blokkal és hagyja figyelmen kívül a hibát:

`dd if=/dev/{{source_drive}} of=/dev/{{dest_drive}} bs={{4194304}} conv={{noerror}}`

- Generáljon egy 100 véletlenszerű bájtból álló fájlt a kernel véletlenszerű meghajtójának használatával:

`dd if=/dev/urandom of={{path/to/random_file}} bs={{100}} count={{1}}`

- Egy lemez írási teljesítményének összehasonlítása:

`dd if=/dev/zero of={{path/to/file_1GB}} bs={{1024}} count={{1000000}}`

- Rendszer biztonsági mentés készítése IMG fájlba:

`dd if={{/dev/drive_device}} of={{path/to/file.img}}`

- Meghajtó visszaállítása IMG fájlból:

`dd if={{path/to/file.img}} of={{/dev/drive_device}}`

- Egy folyamatban lévő dd művelet előrehaladásának ellenőrzése (futtassa ezt a parancsot egy másik shell-ből):

`kill -USR1 $(pgrep ^dd)`
