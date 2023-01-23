# pmount

> Tetszőleges hotpluggolható eszközök normál felhasználóként történő csatlakoztatása. További információ: <https://manned.org/pmount>.

- Egy eszköz csatlakoztatása a `/media/` alatt (az eszköz mount pontként való használata):

`pmount {{/dev/to/block/device}}`

- Egy adott fájlrendszer-típusú eszköz mountolása a `/media/label`:

`pmount --type {{filesystem}} {{/dev/to/block/device}} {{label}}`

- Egy CD-ROM (ISO9660 fájlrendszer típus) mountolása csak olvasható módban:

`pmount --type {{iso9660}} --read-only {{/dev/cdrom}}`

- NTFS-formátumú lemez csatlakoztatása, író-olvasó hozzáférés kikényszerítésével:

`pmount --type {{ntfs}} --read-write {{/dev/sdX}}`

- Az összes csatlakoztatott cserélhető eszköz megjelenítése:

`pmount`
