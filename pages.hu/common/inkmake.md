# inkmake

> GNU Makefile-stílusú SVG exportálás az Inkscape backendjének használatával. További információ: <https://github.com/wader/inkmake>.

- A megadott Inkfile-t végrehajtó SVG fájl exportálása:

`inkmake {{path/to/Inkfile}}`

- Egy Inkfile végrehajtása és részletes információk megjelenítése:

`inkmake --verbose {{path/to/Inkfile}}`

- Egy Inkfile végrehajtása SVG bemeneti fájl(ok) és egy kimeneti fájl megadásával:

`inkmake --svg {{path/to/file.svg}} --out {{path/to/output_image}} {{path/to/Inkfile}}`

- Egy egyéni Inkscape bináris fájl megadása a háttértárként való használathoz:

`inkmake --inkscape {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}`

- Súgó megjelenítése:

`inkmake --help`
