# mlr

> A Miller olyan névvel indexelt adatokhoz, mint a `awk`, `sed`, `cut`, `join` és `sort`, mint a CSV, TSV és a táblázatos JSON. További információ: <https://johnkerl.org/miller/doc>.

- Egy CSV-fájl táblázatos formátumban történő szép-nyomtatása:

`mlr --icsv --opprint cat {{example.csv}}`

- JSON-adatok fogadása és a kimenet pretty printelése:

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- Rendezés ábécé szerint egy mezőn:

`mlr --icsv --opprint sort -f {{field}} {{example.csv}}`

- Rendezés csökkenő numerikus sorrendben egy mezőn:

`mlr --icsv --opprint sort -nr {{field}} {{example.csv}}`

- CSV átalakítása JSON-ná, számítások elvégzése és a számítások megjelenítése:

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}`

- JSON fogadása és a kimenet függőleges JSON formátumban történő formázása:

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- A tömörített CSV fájl sorainak szűrése a számokat karakterláncokként kezelve:

`mlr --prepipe 'gunzip' --csv filter -S '${{fieldName}} =~ "{{regular_expression}}"' {{example.csv.gz}}`
