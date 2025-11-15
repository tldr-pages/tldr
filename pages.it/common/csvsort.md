# csvsort

> Ordina le righe di di file CSV.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

- Ordina un file CSV secondo la colonna 9:

`csvsort -c {{9}} {{data.csv}}`

- Ordina un file CSV secondo la colonna "nome" in ordine decrescente:

`csvsort -r -c {{nome}} {{data.csv}}`

- Ordina un file CSV secondo la colonna 2 e secondo la 4:

`csvsort -c {{2,4}} {{data.csv}}`

- Ordina un file CSV senza inferire il tipo dei dati:

`csvsort --no-inference -c {{colonne}} {{data.csv}}`
