# man

> Kézikönyvoldalak formázása és megjelenítése. További információ: <https://www.man7.org/linux/man-pages/man1/man.1.html>.

- Egy parancs man oldalának megjelenítése:

`man {{command}}`

- A 7. szakaszban található parancs man oldalának megjelenítése:

`man {{7}} {{command}}`

- Egy parancs összes elérhető szakaszának felsorolása:

`man -f {{command}}`

- A manoldalak keresett elérési útvonalának megjelenítése:

`man --path`

- Megjeleníti a manpage helyét, nem pedig magát a manpage-t:

`man -w {{command}}`

- A man-oldal megjelenítése egy adott nyelvterület használatával:

`man {{command}} --locale={{locale}}`

- A keresési karakterláncot tartalmazó manpage-ok keresése:

`man -k "{{search_string}}"`
