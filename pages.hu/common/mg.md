# mg

> Egy kicsi, gyors és hordozható szövegszerkesztő, amely a `emacs` oldalon alapul. További információ: <https://github.com/hboetes/mg>.

- Fájl megnyitása szerkesztéshez:

`mg {{path/to/file}}`

- Egy fájl megnyitása egy megadott sorszámnál:

`mg +{{line_number}} {{path/to/file}}`

- Fájlok megnyitása csak olvasható módban:

`mg -R {{path/to/file1 path/to/file2 ...}}`

- A `~` mentési fájlok letiltása szerkesztés közben:

`mg -n {{path/to/file}}`
