# kwrite

> A KDE Desktop projekt szövegszerkesztője. Lásd még: `kate`. További információ: <https://apps.kde.org/kwrite/>.

- Szöveges fájl megnyitása:

`kwrite {{path/to/file}}`

- Több szöveges fájl megnyitása:

`kwrite {{file1 file2 ...}}`

- Szövegfájl megnyitása egy adott kódolással:

`kwrite --encoding={{UTF-8}} {{path/to/file}}`

- Szövegfájl megnyitása és navigálás egy adott sorra és oszlopra:

`kwrite --line {{line_number}} --column {{column_number}} {{path/to/file}}`
