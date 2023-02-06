# egrep

> Minták keresése fájlokban kiterjesztett reguláris kifejezéssel (támogatja a `?`, `+`, `{}`, `()` és `|`). További információ: <https://manned.org/egrep>.

- Mintázat keresése egy fájlban:

`egrep "{{search_pattern}}" {{path/to/file}}`

- Egy minta keresése több fájlban:

`egrep "{{search_pattern}}" {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Keresés `stdin` egy mintára:

`cat {{path/to/file}} | egrep {{search_pattern}}`

- Minden egyes találat esetén fájlnév és sorszám nyomtatása:

`egrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- Mintakeresés egy könyvtár összes fájljában rekurzívan, a bináris fájlok figyelmen kívül hagyásával:

`egrep --recursive --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- A mintának nem megfelelő sorok keresése:

`egrep --invert-match "{{search_pattern}}" {{path/to/file}}`
