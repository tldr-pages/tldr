# ouch

> Parancssori segédprogram fájlok és könyvtárak tömörítésére és kicsomagolására. További információ: <https://crates.io/crates/ouch>.

- Egy adott fájl kicsomagolása:

`ouch decompress {{path/to/archive.tar.xz}}`

- Egy fájl kicsomagolása egy adott helyre:

`ouch decompress {{path/to/archive.tar.xz}} --dir {{path/to/directory}}`

- Több fájl kicsomagolása:

`ouch decompress {{path/to/archive1.tar path/to/archive2.tar.gz ...}}`

- Fájlok tömörítése:

`ouch compress {{path/to/file1 path/to/file2 ...}} {{path/to/archive.zip}}`
