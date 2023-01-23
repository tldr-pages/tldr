# pax

> Archiválási és másolási segédprogram. További információ: <https://manned.org/pax.1p>.

- Az archívum tartalmának listázása:

`pax -f {{archive.tar}}`

- Egy gzippelt archívum tartalmának listázása:

`pax -zf {{archive.tar.gz}}`

- Archívum létrehozása fájlokból:

`pax -wf {{target.tar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Archívum létrehozása fájlokból, kimeneti átirányítással:

`pax -w {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} > {{target.tar}}`

- Archívum kicsomagolása az aktuális könyvtárba:

`pax -rf {{source.tar}}`

- Másolás egy könyvtárba, az eredeti metaadatok megtartása mellett; a `target/` címnek léteznie kell:

`pax -rw {{path/to/file1}} {{path/to/directory1}} {{path/to/directory2}} {{target/}}`
