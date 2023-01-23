# sfill

> A megadott könyvtárat tartalmazó partíció szabad helyének és inode-jainak biztonságos felülírása. További információ: <https://manned.org/sfill>.

- A lemez szabad helyének és inode-jainak felülírása 38 írással (lassú, de biztonságos):

`sfill {{/path/to/mounted_disk_directory}}`

- Egy lemez szabad helyének és inode-jainak felülírása 6 írással (gyors, de kevésbé biztonságos) és állapot megjelenítése:

`sfill -l -v {{/path/to/mounted_disk_directory}}`

- Egy lemez szabad helyének és inode-jainak felülírása 1 írással (nagyon gyors, de nem biztonságos) és állapot megjelenítése:

`sfill -ll -v {{/path/to/mounted_disk_directory}}`

- A lemeznek csak a szabad helyét írja felül:

`sfill -I {{/path/to/mounted_disk_directory}}`

- Csak a lemez szabad inode-jainak felülírása:

`sfill -i {{/path/to/mounted_disk_directory}}`
