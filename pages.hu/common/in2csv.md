# in2csv

> Különböző táblázatos adatformátumok átalakítása CSV-be. Csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>.

- XLS fájl átalakítása CSV-be:

`in2csv {{data.xls}}`

- DBF fájl átalakítása CSV fájlba:

`in2csv {{data.dbf}} > {{data.csv}}`

- Egy XLSX fájl egy adott lapjának átalakítása CSV-be:

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- JSON fájl átvezetése az in2csv-be:

`cat {{data.json}} | in2csv -f json > {{data.csv}}`
