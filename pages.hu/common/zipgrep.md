# zipgrep

> A ZIP-archívumban található fájlokban található minták keresése kiterjesztett reguláris kifejezések segítségével (támogatja a `?`, `+`, `{}`, `()` és `|`). További információ: [https://manned.org/zipgrep.](https://manned.org/zipgrep)

- Minta keresése egy ZIP-archívumban:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}}`

- Minden egyes találathoz kiírja a fájl nevét és a sorszámot:

`zipgrep -H -n "{{search_pattern}}" {{path/to/file.zip}}`

- A mintának nem megfelelő sorok keresése:

`zipgrep -v "{{search_pattern}}" {{path/to/file.zip}}`

- ZIP-archívumon belüli fájlok megadása a keresésből:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} {{file/to/search1}} {{file/to/search2}}`

- ZIP-archívumon belüli fájlok kizárása a keresésből:

`zipgrep "{{search_pattern}}" {{path/to/file.zip}} -x {{file/to/exclude1}} {{file/to/exclude2}}`
