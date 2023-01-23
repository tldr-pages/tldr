# bzegrep

> Bővített reguláris kifejezések mintáinak keresése bzip2 tömörített fájlokban az egrep segítségével. További információ: <https://manned.org/bzegrep>.

- Kiterjesztett reguláris kifejezések keresése (támogatja a `?`, `+`, `{}`, `()` és `|`) egy tömörített fájlban (nagy- és kisbetű-érzékeny):

`bzegrep "{{search_pattern}}" {{path/to/file}}`

- Kiterjesztett reguláris kifejezések keresése (támogatja a `?`, `+`, `{}`, `()` és `|`) egy tömörített fájlban (esetfüggetlen):

`bzegrep --ignore-case "{{search_pattern}}" {{path/to/file}}`

- A mintának nem megfelelő sorok keresése:

`bzegrep --invert-match "{{search_pattern}}" {{path/to/file}}`

- A fájl nevének és a sorszámnak a kiírása minden egyes találathoz:

`bzegrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- A mintának megfelelő sorok keresése, csak az egyező szöveget nyomtatva ki:

`bzegrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- A bzip2 tömörített tar-archívumban lévő fájlok rekurzív keresése egy minta alapján:

`bzegrep --recursive "{{search_pattern}}" {{path/to/file}}`
