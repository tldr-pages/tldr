# zstd

> Fájlok tömörítése vagy dekompressziója Zstandard tömörítéssel. További információ: <https://github.com/facebook/zstd>.

- Egy fájl tömörítése egy új fájlba a `.zst` utótaggal:

`zstd {{path/to/file}}`

- Egy fájl kitömörítése:

`zstd -d {{path/to/file}}.zst`

- Dekompresszálás a `stdout` címre:

`zstd -dc {{path/to/file}}.zst`

- Egy fájl tömörítése a tömörítési szint megadásával, ahol 1=leggyorsabb, 19=leglassabb és 3=alapértelmezett:

`zstd -{{level}} {{path/to/file}}`

- A magasabb tömörítési szintek (22-ig) feloldása több memóriát igényel (mind a tömörítéshez, mind a dekompresszióhoz):

`zstd --ultra -{{level}} {{path/to/file}}`
