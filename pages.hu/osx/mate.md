# mate

> Általános célú szövegszerkesztő macOS-re. További információ: <https://macromates.com/>.

- Indítsa el a TextMate-et:

`mate`

- Meghatározott fájlok megnyitása:

`mate {{path/to/file1 path/to/file2 ...}}`

- Adja meg egy fájl fájltípusát:

`mate --type {{filetype}} {{path/to/file}}`

- Megnyitás és várakozás egy adott fájl szerkesztésének befejezéséig:

`mate --wait {{path/to/file}}`

- Fájl megnyitása úgy, hogy a kurzor egy adott soron és oszlopon álljon:

`mate --line {{line_number}}:{{column_number}} {{path/to/file}}`
