# ab

> Strumento di benchmarking per il server HTTP Apache.
> Maggiori informazioni: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Esegue 100 richieste HTTP GET verso un dato URL:

`ab -n 100 {{url}}`

- Esegue 100 richieste HTTP GET in batch concorrenti da 10 verso un URL:

`ab -n 100 -c 10 {{url}}`

- Esegue 100 richieste HTTP POST verso un URL usando un payload JSON da file:

`ab -n 100 -T {{application/json}} -p {{percorso/al/file.json}} {{url}}`

- Usa HTTP [k]eep-Alive (più richieste nella stessa sessione HTTP):

`ab -k {{url}}`

- Imposta il timeout massimo in secondi per il benchmarking (30 di default):

`ab -t {{60}} {{url}}`

- Salva i risultati in un file CSV:

`ab -e {{percorso/al/file.csv}}`
