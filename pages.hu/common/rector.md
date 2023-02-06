# rector

> Automatizált eszköz a PHP 5.3+ kód frissítéséhez és refaktorálásához. További információ: <https://github.com/rectorphp/rector>.

- Egy adott könyvtár feldolgozása:

`rector process {{path/to/directory}}`

- Egy könyvtár feldolgozása változtatások alkalmazása nélkül (száraz futtatás):

`rector process {{path/to/directory}} --dry-run`

- Egy könyvtár feldolgozása és kódolási szabványok alkalmazása:

`rector process {{path/to/directory}} --with-style`

- Az elérhető szintek listájának megjelenítése:

`rector levels`

- Egy könyvtár feldolgozása egy adott szinten:

`rector process {{path/to/directory}} --level {{level_name}}`
