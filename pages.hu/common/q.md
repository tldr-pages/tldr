# q

> SQL-szerű lekérdezések végrehajtása .csv és .tsv fájlokon. További információ: <https://harelba.github.io/q>.

- A `.csv` fájl lekérdezése az elválasztójel ',' megadásával:

`q -d',' "SELECT * from {{path/to/file}}"`

- A `.tsv` fájl lekérdezése:

`q -t "SELECT * from {{path/to/file}}"`

- Fájl lekérdezése fejléc sorral:

`q -d{{delimiter}} -H "SELECT * from {{path/to/file}}"`

- Adatok beolvasása a `stdin` oldalról ; a lekérdezésben a '-' a `stdin` oldalról származó adatokat jelöli:

`{{output}} | q "select * from -"`

- Két fájl (a példában `f1` és `f2` néven) összekapcsolása a `c1`, egy közös oszlopon:

`q "SELECT * FROM {{path/to/file}} f1 JOIN {{path/to/other_file}} f2 ON (f1.c1 = f2.c1)"`

- Kimenet formázása kimeneti elválasztójel és kimeneti fejléc sor használatával (megjegyzés: a parancs az oszlopneveket a bemeneti fájl fejlécén vagy a lekérdezésben felülbírált oszlop aliasokon alapuló oszlopnevek alapján adja ki):

`q -D{{delimiter}} -O "SELECT {{column}} as {{alias}} from {{path/to/file}}"`
