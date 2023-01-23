# xml pyx

> XML dokumentum átalakítása PYX (ESIS - ISO 8879) formátumba. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- XML dokumentum átalakítása PYX formátumba:

`xml pyx {{path/to/input.xml|URI}} > {{path/to/output.pyx}}`

- XML-dokumentum konvertálása a `stdin` formátumból PYX formátumba:

`cat {{path/to/input.xml}} | xml pyx > {{path/to/output.pyx}}`

- A `pyx` alparancs súgójának megjelenítése:

`xml pyx --help`
