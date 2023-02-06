# xml elements

> Egy XML-dokumentum elemeinek kivonása és szerkezetének megjelenítése. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- Elemek kivonása egy XML-dokumentumból (XPATH-kifejezések előállítása):

`xml elements {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- Elemek és attribútumaik kivonása egy XML-dokumentumból:

`xml elements -a {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- Elemek, attribútumaik és értékeik kivonása XML-dokumentumból:

`xml elements -v {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}`

- Egy XML-dokumentum rendezett egyedi elemeinek kinyomtatása a dokumentum szerkezetének megtekintéséhez:

`xml elements -u {{path/to/input.xml|URI}}`

- Rendezett egyedi elemek nyomtatása egy XML-dokumentumból 3 mélységig:

`xml elements -d{{3}} {{path/to/input.xml|URI}}`

- A `elements` alparancs súgójának megjelenítése:

`xml elements --help`
