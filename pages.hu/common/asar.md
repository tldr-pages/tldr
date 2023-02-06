# asar

> Fájlarchiváló az Electron platformhoz. További információ: <https://github.com/electron/asar>.

- Fájl vagy könyvtár archiválása:

`asar pack {{path/to/file_or_directory}} {{archived.asar}}`

- Archívum kicsomagolása:

`asar extract {{archived.asar}}`

- Egy adott fájl kivonása egy archívumból:

`asar extract-file {{archived.asar}} {{file}}`

- Egy archív fájl tartalmának listázása:

`asar list {{archived.asar}}`
