# in2csv

> Convertește diferite formate de date tabelare în CSV.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>

- Conversia unui fișier XLS în CSV:

`in2csv {{data.xls}}`

- Conversia unui fişier DBF într-un fişier CSV:

`in2csv {{data.dbf}} > {{data.csv}}`

- Conversia unei anumite foi dintr-un fișier XLSX la CSV:

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- Țeavă un fișier JSON la in2csv:

`cat {{data.json}} | in2csv -f json > {{data.csv}}`
