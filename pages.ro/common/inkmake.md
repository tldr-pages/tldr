# inkmake

> Exportul SVG în stil GNU Makefile utilizând backendul Inkscape.
> Mai multe informaţii: <https://github.com/wader/inkmake>

- Exportați un fișier SVG care execută fișierul Inkfile specificat:

`inkmake {{path/to/Inkfile}}`

- Executați un fișier de cerneală și afișați informații detaliate:

`inkmake --verbose {{path/to/Inkfile}}`

- Executați un fișier de cerneală, specificând fișierul (fișierele) de intrare SVG și un fișier de ieșire:

`inkmake --svg {{path/to/file.svg}} --out {{path/to/output_image}} {{path/to/Inkfile}}`

- Specificați un binar personalizat Inkscape pentru a utiliza ca backend:

`inkmake --inkscape {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}`

- Ajutor pentru afișare:

`inkmake --help`
