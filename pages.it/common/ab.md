# ab

> Strumento di benchmarking di Apache. Il più semplice modo per eseguire un test sul carico del server.
> Maggiori informazioni: <https://httpd.apache.org/docs/2.4/programs/ab.html>.

- Esegui 100 richieste HTTP GET ad un dato URL:

`ab -n {{100}} {{url}}`

- Esegui 100 richieste HTTP GET ad un dato url, processandone fino a 10 requests contemporaneamente:

`ab -n {{100}} -c {{10}} {{url}}`

- Usa keep alive:

`ab -k {{url}}`

- Setta il massimo numero di secondi per il benchmarking:

`ab -t {{secondi}} {{url}}`
