# xml canonic

> XML dokumentumok kanonikussá tétele. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- XML-dokumentum kanonikussá tétele a megjegyzések megőrzésével:

`xml canonic {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- XML-dokumentum kanonikussá tétele, a megjegyzések eltávolítása:

`xml canonic --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- Kizárólag XML dokumentum kanonikussá tétele, XPATH használatával egy fájlból, a megjegyzések megtartásával:

`xml canonic --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- A `canonic` alparancs súgójának megjelenítése:

`xml canonic --help`
