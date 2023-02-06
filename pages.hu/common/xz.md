# xz

> .xz és .lzma fájlok tömörítése vagy kicsomagolása. További információ: <https://tukaani.org/xz/format.html>.

- Egy fájl tömörítése xz fájlformátumba:

`xz {{path/to/file}}`

- Egy xz fájl kicsomagolása:

`xz -d {{file.xz}}`

- Fájl tömörítése LZMA fájlformátumba:

`xz --format={{lzma}} {{path/to/file}}`

- LZMA fájl dekompressziója:

`xz -d --format={{lzma}} {{file.lzma}}`

- Egy fájl kicsomagolása és írása a `stdout` címre:

`xz -dc {{file.xz}}`

- Egy fájl tömörítése, de ne törölje az eredetit:

`xz -k {{path/to/file}}`

- Egy fájl tömörítése a leggyorsabb tömörítéssel:

`xz -0 {{path/to/file}}`

- Tömörítés a legjobb tömörítéssel:

`xz -9 {{path/to/file}}`
