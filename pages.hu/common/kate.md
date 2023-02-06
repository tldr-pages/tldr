# kate

> A KDE fejlett szövegszerkesztője. További információ: <https://kate-editor.org/>.

- Meghatározott fájlok megnyitása:

`kate {{path/to/file1 path/to/file2 ...}}`

- Konkrét távoli fájlok megnyitása:

`kate {{https://example.com/path/to/file1 https://example.com/path/to/file2 ...}}`

- Új szerkesztőpéldány létrehozása akkor is, ha egy már nyitva van:

`kate --new`

- Fájl megnyitása úgy, hogy a kurzor egy adott soron áll:

`kate --line {{line_number}} {{path/to/file}}`

- Fájl megnyitása a kurzorral az adott soron és oszlopon:

`kate --line {{line_number}} --column {{column_number}} {{path/to/file}}`

- Fájl létrehozása a `stdin` címen:

`cat {{path/to/file}} | kate --stdin`

- Súgó megjelenítése:

`kate --help`
