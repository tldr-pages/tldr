# grep

> Minták keresése fájlokban szabályos kifejezések segítségével. További információ: <https://www.gnu.org/software/grep/manual/grep.html>.

- Mintázat keresése egy fájlban:

`grep "{{search_pattern}}" {{path/to/file}}`

- Pontos karakterlánc keresése (kikapcsolja a reguláris kifejezéseket):

`grep --fixed-strings "{{exact_string}}" {{path/to/file}}`

- Mintát keres egy könyvtárban rekurzívan az összes fájlban, a találatok sorszámainak megjelenítésével, a bináris fájlok figyelmen kívül hagyásával:

`grep --recursive --line-number --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- Kiterjesztett reguláris kifejezések használata (támogatja a `?`, `+`, `{}`, `()` és `|`), nagy- és kisbetűket nem érzékelő módban:

`grep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 3 sor kontextus kiírása minden találat körül, előtt vagy után:

`grep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- A fájlnév és a sorszám nyomtatása minden egyes találathoz színes kimenettel:

`grep --with-filename --line-number --color=always "{{search_pattern}}" {{path/to/file}}`

- A mintának megfelelő sorok keresése, csak az egyező szöveget nyomtatva ki:

`grep --only-matching "{{search_pattern}}" {{path/to/file}}`

- Keresés a `stdin` oldalon a mintának nem megfelelő sorok után:

`cat {{path/to/file}} | grep --invert-match "{{search_pattern}}"`
