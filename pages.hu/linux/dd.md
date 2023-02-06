# dd

> Fájlok átalakítása és másolása. További információ: <https://www.gnu.org/software/coreutils/dd>.

- Készítsen bootolható USB-meghajtót egy izohibrid fájlból (pl. `archlinux-xxx.iso`), és mutassa meg a folyamatot:

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- Egy meghajtó klónozása egy másik meghajtóra 4 MiB-os blokkkal, a hiba figyelmen kívül hagyása és a haladás megjelenítése:

`dd if={{/dev/source_drive}} of={{/dev/dest_drive}} bs={{4M}} conv={{noerror}} status=progress`

- Egy 100 véletlenszerű bájtból álló fájl létrehozása a kernel véletlenszerű meghajtójának használatával:

`dd if=/dev/urandom of={{path/to/random_file}} bs={{100}} count={{1}}`

- Egy lemez írási teljesítményének összehasonlítása:

`dd if=/dev/zero of={{path/to/file_1GB}} bs={{1024}} count={{1000000}}`

- Rendszer mentés készítése IMG fájlba, és a folyamat bemutatása:

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`

- Egy meghajtó visszaállítása egy IMG-fájlból és a folyamat bemutatása:

`dd if={{path/to/file.img}} of={{/dev/drive_device}} status=progress`

- Egy folyamatban lévő dd művelet előrehaladásának ellenőrzése (futtassa ezt a parancsot egy másik shell-ből):

`kill -USR1 $(pgrep ^dd)`
