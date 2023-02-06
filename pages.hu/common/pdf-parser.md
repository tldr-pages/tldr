# pdf-parser

> A PDF-fájl alapvető elemeinek azonosítása a fájl renderelése nélkül. További információ: <https://blog.didierstevens.com/programs/pdf-tools>.

- Egy PDF-fájl statisztikáinak megjelenítése:

`pdf-parser --stats {{path/to/file.pdf}}`

- A `/Font` típusú objektumok megjelenítése egy PDF-fájlban:

`pdf-parser --type={{/Font}} {{path/to/file.pdf}}`

- Sztringek keresése közvetett objektumokban:

`pdf-parser --search={{search_string}} {{path/to/file.pdf}}`
