# megatools-dl

> Letöltés a `mega.nz` oldalról. A `megatools` csomag része. További információ: <https://megatools.megous.com/man/megatools-dl.html>.

- Fájlok letöltése a `mega.nz` linkről az aktuális könyvtárba:

`megatools-dl {{https://mega.nz/...}}`

- Fájlok letöltése a `mega.nz` linkről egy adott könyvtárba:

`megatools-dl --path {{path/to/directory}} {{https://mega.nz/...}}`

- Interaktívan kiválaszthatja, hogy mely fájlokat kívánja letölteni:

`megatools-dl --choose-files {{https://mega.nz/...}}`

- A letöltési sebesség korlátozása KiB/s-ban:

`megatools-dl --limit-speed {{speed}} {{https://mega.nz/...}}`
