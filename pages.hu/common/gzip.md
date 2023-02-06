# gzip

> Fájlok tömörítése/tömörítés feloldása gzip tömörítéssel (LZ77). További információ: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Egy fájl tömörítése, kicserélve azt egy gzippel tömörített verzióra:

`gzip {{file.ext}}`

- Egy fájl kitömörítése, az eredeti tömörítetlen verzióval való helyettesítése:

`gzip -d {{file.ext}}.gz`

- Egy fájl tömörítése, megtartva az eredeti fájlt:

`gzip --keep {{file.ext}}`

- Egy fájl tömörítése a kimeneti fájlnév megadásával:

`gzip -c {{file.ext}} > {{compressed_file.ext.gz}}`

- A kimeneti fájlnevet megadó gzippelt fájl kicsomagolása:

`gzip -c -d {{file.ext}}.gz > {{uncompressed_file.ext}}`

- A tömörítési szint megadása. 1=A leggyorsabb (legrosszabb), 9=leglassabb (legjobb), Az alapértelmezett szint 6:

`gzip -9 -c {{file.ext}} > {{compressed_file.ext.gz}}`
