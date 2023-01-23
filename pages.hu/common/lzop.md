# lzop

> Fájlok tömörítése vagy dekompressziója LZO tömörítéssel. További információ: <https://www.lzop.org/>.

- Egy fájl tömörítése egy új fájlba a `.lzo` utótaggal:

`lzop {{path/to/file}}`

- Egy fájl kitömörítése:

`lzop -d {{path/to/file}}.lzo`

- Egy fájl tömörítése a tömörítési szint megadásával. 0 = legrosszabb, 9 = legjobb (az alapértelmezett szint 3):

`lzop -{{level}} {{path/to/file}}`
