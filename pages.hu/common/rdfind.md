# rdfind

> Keresse meg a duplikált tartalmú fájlokat, és szabaduljon meg tőlük. További információ: <https://rdfind.pauldreik.se>.

- Azonosítja az összes duplikátumot egy adott könyvtárban, és kiad egy összefoglalót:

`rdfind -dryrun true {{path/to/directory}}`

- Az összes duplikátumot hardlinkkel helyettesíti:

`rdfind -makehardlinks true {{path/to/directory}}`

- Az összes duplikátum helyettesítése symlinkekkel/lágy linkekkel:

`rdfind -makesymlinks true {{path/to/directory}}`

- Törölje az összes duplikátumot, és ne hagyja figyelmen kívül az üres fájlokat:

`rdfind -deleteduplicates true -ignoreempty false {{path/to/directory}}`
