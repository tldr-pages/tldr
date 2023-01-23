# lz4

> .lz4 fájlok tömörítése vagy dekompressziója. További információ: <https://github.com/lz4/lz4>.

- Egy fájl tömörítése:

`lz4 {{path/to/file}}`

- Egy fájl kicsomagolása:

`lz4 -d {{file.lz4}}`

- Egy fájl kicsomagolása és írása a `stdout` címre:

`lz4 -dc {{file.lz4}}`

- Egy könyvtár és tartalmának csomagolása és tömörítése:

`tar cvf - {{path/to/directory}} | lz4 - {{dir.tar.lz4}}`

- Egy könyvtár és tartalma kicsomagolása és kicsomagolása:

`lz4 -dc {{dir.tar.lz4}} | tar -xv`

- Egy fájl tömörítése a legjobb tömörítéssel:

`lz4 -9 {{path/to/file}}`
