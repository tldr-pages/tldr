# xml depyx

> PYX (ESIS - ISO 8879) dokumentum átalakítása XML formátumba. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- PYX (ESIS - ISO 8879) dokumentum átalakítása XML formátumba:

`xml depyx {{path/to/input.pyx|URI}} > {{path/to/output.xml}}`

- PYX dokumentum konvertálása a `stdin` oldalról XML formátumba:

`cat {{path/to/input.pyx}} | xml depyx > {{path/to/output.xml}}`

- A `depyx` alparancs súgójának megjelenítése:

`xml depyx --help`
