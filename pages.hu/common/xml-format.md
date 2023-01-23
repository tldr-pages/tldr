# xml format

> XML dokumentum formázása. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- XML-dokumentum formázása, behúzás tabulátorokkal:

`xml format --indent-tab {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- HTML-dokumentum formázása, behúzás 4 szóközzel:

`xml format --html --indent-spaces {{4}} {{path/to/input.html|URI}} > {{path/to/output.html}}`

- A rosszul formált XML-dokumentum elemezhető részeinek visszanyerése, behúzás nélkül:

`xml format --recover --noindent {{path/to/malformed.xml|URI}} > {{path/to/recovered.xml}}`

- XML-dokumentum formázása a `stdin` oldalról, a `DOCTYPE` deklaráció eltávolításával:

`cat {{path\to\input.xml}} | xml format --dropdtd > {{path/to/output.xml}}`

- XML-dokumentum formázása, az XML-nyilatkozat elhagyása:

`xml format --omit-decl {{path\to\input.xml|URI}} > {{path/to/output.xml}}`

- A `format` alparancs súgójának megjelenítése:

`xml format --help`
