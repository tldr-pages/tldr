# sdcv

> StarDict, egy parancssori szótár kliens. A szótárakat a klienstől külön biztosítjuk. További információ: <https://manned.org/sdcv>.

- Az sdcv interaktív indítása:

`sdcv`

- Telepített szótárak listája:

`sdcv --list-dicts`

- Egy adott szótár definíciójának megjelenítése:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Definíció keresése fuzzy kereséssel:

`sdcv {{search_term}}`

- Definíció keresése pontos kereséssel:

`sdcv --exact-search {{search_term}}`

- Definíció keresése és a kimenet JSON formátumban történő formázása:

`sdcv --json {{search_term}}`

- Szótárak keresése egy adott könyvtárban:

`sdcv --data-dir {{path/to/directory}} {{search_term}}`
