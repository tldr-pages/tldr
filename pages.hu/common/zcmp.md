# zcmp

> Tömörített fájlok összehasonlítása. További információ: <https://manned.org/zcmp>.

- A `cmp` meghívása két, a `gzip` segítségével tömörített fájlra:

`zcmp {{path/to/file1.gz}} {{path/to/file2.gz}}`

- Egy fájl összehasonlítása a gzippelt változatával (feltéve, hogy a `.gz` már létezik):

`zcmp {{path/to/file}}`
