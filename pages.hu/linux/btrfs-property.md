# btrfs property

> Egy adott btrfs fájlrendszer objektum (fájlok, könyvtárak, alkötetek, fájlrendszerek vagy eszközök) tulajdonságainak lekérése, beállítása vagy listázása. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- Az adott btrfs objektum elérhető tulajdonságainak (és leírásainak) listázása:

`sudo btrfs property list {{path/to/btrfs_object}}`

- Az adott btrfs objektum összes tulajdonságának lekérdezése:

`sudo btrfs property get {{path/to/btrfs_object}}`

- Az adott btrfs fájlrendszer vagy eszköz `label` tulajdonságának lekérdezése:

`sudo btrfs property get {{path/to/btrfs_filesystem}} label`

- Az adott btrfs fájlrendszer vagy eszköz összes objektumtípus-specifikus tulajdonságának lekérdezése:

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{path/to/btrfs_filesystem}}`

- A `compression` tulajdonság beállítása egy adott btrfs inode (fájl vagy könyvtár) számára:

`sudo btrfs property set {{path/to/btrfs_inode}} compression {{zstd|zlib|lzo|none}}`
