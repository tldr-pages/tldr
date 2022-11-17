# csvstat

> Stampa statistiche descrittive per tutte le colonne di un file CSV.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- Mostra tutte le statistiche per tutte le colonne:

`csvstat {{dati.csv}}`

- Mostra tutte le statistiche per le colonne 2 e 4:

`csvstat -c {{2,4}} {{dati.csv}}`

- Mostra la somma per tutte le colonne:

`csvstat --sum {{dati.csv}}`

- Mostra la lunghezza massima dei valori della colonna 3:

`csvstat -c {{3}} --len {{dati.csv}}`

- Mostra il numero di valori unici nella colonna "nome":

`csvstat -c {{nome}} --unique {{dati.csv}}`
