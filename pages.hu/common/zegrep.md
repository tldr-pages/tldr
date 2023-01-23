# zegrep

> Kiterjesztett reguláris kifejezésminták keresése tömörített fájlokban a `egrep` segítségével. További információ: [https://www.unix.com/man-page/freebsd/1/zegrep/.](https://www.unix.com/man-page/freebsd/1/zegrep/)

- Kiterjesztett reguláris kifejezések keresése (támogatja a `?`, `+`, `{}`, `()` és `|`) egy tömörített fájlban (nagy- és kisbetű-érzékeny):

`zegrep "{{search_pattern}}" {{path/to/file}}`

- Kiterjesztett reguláris kifejezések keresése (támogatja a `?`, `+`, `{}`, `()` és `|`) egy tömörített fájlban (eset-érzékelés nélkül):

`zegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- A mintának nem megfelelő sorok keresése:

`zegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- A fájl nevének és a sorszámnak a kiírása minden egyes találathoz:

`zegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- A mintának megfelelő sorok keresése, csak az egyező szöveget nyomtatva ki:

`zegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- A tömörített fájlban lévő fájlok rekurzív keresése egy minta alapján:

`zegrep --recursive "{{search_pattern}}" {{path/to/file}}`
