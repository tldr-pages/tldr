# bzfgrep

> A bzip2 tömörített fájlokban új sorokkal elválasztott rögzített karakterláncok keresése fgrep segítségével. További információ: <https://manned.org/bzfgrep>.

- Új sorokkal elválasztott keresési karakterláncok listájának megfelelő sorok keresése egy tömörített fájlban (nagy- és kisbetű-érzékeny):

`bzfgrep "{{search_string}}" {{path/to/file}}`

- A tömörített fájlban új sorokkal elválasztott keresési karakterláncok listájának megfelelő sorok keresése (nem érzékeli a nagy- és kisbetűket):

`bzfgrep --ignore-case "{{search_string}}" {{path/to/file}}`

- A tömörített fájlban új sorokkal elválasztott keresési karakterláncok listájával nem egyező sorok keresése:

`bzfgrep --invert-match "{{search_string}}" {{path/to/file}}`

- A fájl nevének és a sorszámnak a nyomtatása minden egyes találathoz:

`bzfgrep --with-filename --line-number "{{search_string}}" {{path/to/file}}`

- A mintának megfelelő sorok keresése, csak az egyező szöveget nyomtatva ki:

`bzfgrep --only-matching "{{search_string}}" {{path/to/file}}`

- A bzip2 tömörített tar archívumban lévő fájlok rekurzív keresése a megadott karakterláncok listája alapján:

`bzfgrep --recursive "{{search_string}}" {{path/to/file}}`
