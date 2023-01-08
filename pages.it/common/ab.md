# ab

> Strumento di benchmarking di Apache. Il più semplice modo per eseguire un test sul carico del server.
> Maggiori informazioni: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Esegui 100 richieste HTTP GET ad un dato URL:

`ab -n {{100}} {{url}}`

- Esegui 100 richieste HTTP GET ad un dato URL, processandone fino a 10 contemporaneamente:

`ab -n {{100}} -c {{10}} {{url}}`

- Esegui 100 richieste HTTP POST a un dato URL, utilizzando un payload JSON tramite file:

`ab -n {{100}} -T {{application/json}} -p {{percorso/del/file.json}} {{url}}`

- Usa HTTP [K]eep Alive, ovvero esegui richieste multiple in una stessa sessione HTTP:

`ab -k {{url}}`

- Setta il massimo numero di secondi per il benchmarking:

`ab -t {{secondi}} {{url}}`
