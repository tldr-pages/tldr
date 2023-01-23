# man

> Kézikönyvoldalak formázása és megjelenítése. További információ: <https://manned.org/man>.

- Egy parancs man oldalának megjelenítése:

`man {{command}}`

- A 7. szakaszban található parancs man oldalának megjelenítése:

`man {{7}} {{command}}`

- Egy parancs összes elérhető szakaszának felsorolása:

`man --whatis {{command}}`

- A manoldalak keresett elérési útvonalának megjelenítése:

`man --path`

- Megjeleníti a manpage helyét, nem pedig magát a manpage-t:

`man --where {{command}}`

- A man-oldal megjelenítése egy adott nyelvterület használatával:

`man --locale={{locale}} {{command}}`

- A keresési karakterláncot tartalmazó manpage-ok keresése:

`man --apropos "{{search_string}}"`
