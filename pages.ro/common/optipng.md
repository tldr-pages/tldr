# optipng

> Utilitar de optimizare a fișierelor de imagine PNG.
> Mai multe informaţii: <http://optipng.sourceforge.net>

- Comprimați un PNG cu setările implicite:

`optipng {{path/to/file.png}}`

- Comprimați un PNG cu cea mai bună compresie:

`optipng -o{{7}} {{path/to/file.png}}`

- Comprimați un PNG cu cea mai rapidă compresie:

`optipng -o{{0}} {{path/to/file.png}}`

- Comprimați un PNG și adăugați intercalarea:

`optipng -i {{1}} {{path/to/file.png}}`

- Comprimați un PNG și păstrați toate metadatele (inclusiv marcajele temporale ale fișierelor):

`optipng -preserve {{path/to/file.png}}`

- Comprimați un PNG și eliminați toate metadatele:

`optipng -strip all {{path/to/file.png}}`
