# brotli

> Fájlok tömörítése/tömörítés feloldása Brotli tömörítéssel. További információ: <https://github.com/google/brotli>.

- Egy fájl tömörítése, létrehozva egy tömörített változatot a fájl mellett:

`brotli {{file.ext}}`

- Egy fájl kitömörítése, létrehozva egy tömörítetlen változatot a fájl mellett:

`brotli -d {{file.ext}}.br`

- Egy fájl tömörítése a kimeneti fájlnév megadásával:

`brotli {{file.ext}} -o {{compressed_file.ext.br}}`

- A kimeneti fájlnevet megadó Brotli fájl kicsomagolása:

`brotli -d {{compressed_file.ext.br}} -o {{file.ext}}`

- A tömörítési szint megadása. 1=A leggyorsabb (legrosszabb), 11=leglassabb (legjobb):

`brotli -q {{11}} {{file.ext}} -o {{compressed_file.ext.br}}`
