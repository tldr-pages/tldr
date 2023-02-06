# ptargrep

> Szabályos kifejezésminták keresése egy vagy több tar archívumfájlban. További információ: <https://manned.org/ptargrep>.

- Egy minta keresése egy tar-fájlban:

`ptargrep "{{search_pattern}}" {{path/to/file}}`

- Egy minta keresése több fájlban:

`ptargrep "{{search_pattern}}" {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Kivonatolás az aktuális könyvtárba az archívumból származó fájl alapneve alapján:

`ptargrep --basename "{{search_pattern}}" {{path/to/file}}`

- Nagy- és kisbetűket nem érzékelő minta keresése egy tar-fájlon belül:

`ptargrep --ignore-case "{{search_pattern}}" {{path/to/file}}`
