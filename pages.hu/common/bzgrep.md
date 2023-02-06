# bzgrep

> A bzip2 tömörített fájlokban található minták keresése grep segítségével. További információ: <https://manned.org/bzgrep>.

- Minta keresése egy tömörített fájlban:

`bzgrep "{{search_pattern}}" {{path/to/file}}`

- Kiterjesztett reguláris kifejezések használata (támogatja a `?`, `+`, `{}`, `()` és `|`), a nagy- és kisbetűket nem érzékelő módban:

`bzgrep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- 3 sor kontextus kiírása minden találat körül, előtt vagy után:

`bzgrep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- A fájl nevének és sorszámának nyomtatása minden egyes találathoz:

`bzgrep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- A mintának megfelelő sorok keresése, csak az egyező szöveget nyomtatva:

`bzgrep --only-matching "{{search_pattern}}" {{path/to/file}}`

- A bzip2 tömörített tar archívumban lévő fájlok rekurzív keresése egy minta alapján:

`bzgrep --recursive "{{search_pattern}}" {{path/to/tar/file}}`

- A `stdin` oldalon kereshet olyan sorokat, amelyek nem egyeznek meg egy mintával:

`cat {{/path/to/bz/compressed/file}} | bzgrep --invert-match "{{search_pattern}}"`
