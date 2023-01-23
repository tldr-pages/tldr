# csvkit

> A CSV-fájlok manipulációs eszköztára. Lásd az egyes parancsokat: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`. További információ: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- Futtasson parancsot egy CSV-fájlon egyéni elválasztójelekkel:

`{{cmd}} -d {{delimiter}} {{filename.csv}}`

- Parancs futtatása CSV-fájlon tabulátorral, mint elválasztójel (felülírja a -d parancsot):

`{{cmd}} -t {{filename.csv}}`

- Parancs futtatása CSV-fájlon egyéni idézőjellel:

`{{cmd}} -q {{quote_char}} {{filename.csv}}`

- Parancs futtatása CSV-fájlon fejléc nélküli sorral:

`{{cmd}} -H {{filename.csv}}`
