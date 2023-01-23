# textql

> SQL végrehajtása strukturált szöveg, például csv vagy tsv fájlok ellen. További információ: <https://github.com/dinedal/textql>.

- A megadott `.csv` fájl azon sorainak kinyomtatása, amelyek megfelelnek egy SQL-kérdésnek, a `stdout` címre:

`textql -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- `.tsv` fájl lekérdezése:

`textql -dlm=tab -sql "{{SELECT * FROM filename}}" {{path/to/filename.tsv}}`

- Lekérdezési fájl a fejléc sorával:

`textql -dlm={{delimiter}} -header -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- Adatok beolvasása a `stdin`:

`cat {{path/to/file}} | textql -sql "{{SELECT * FROM stdin}}"`

- Két fájl összekapcsolása egy megadott közös oszlopon:

`textql -header -sql "SELECT * FROM {{file1}} JOIN {{file2}} ON {{file1}}.{{c1}} = {{file2}}.{{c1}} LIMIT {{10}}" -output-header {{path/to/file1.csv}} {{path/to/file2.csv}}`

- Kimenet formázása kimeneti elválasztójel és kimeneti fejléc sor használatával:

`textql -output-dlm={{delimiter}} -output-header -sql "SELECT {{column}} AS {{alias}} FROM {{filename}}" {{path/to/filename.csv}}`
