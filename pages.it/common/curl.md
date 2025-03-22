# curl

> Trasferisci dati da o ad un server.
> Supporta la maggior parte dei protocolli, tra cui HTTP, HTTPS, FTP, SCP, etc.
> Maggiori informazioni: <https://curl.se/docs/manpage.html>.

- Esegue una richiesta HTTP GET e stampa il contenuto in `stdout`:

`curl {{https://example.com}}`

- Esegue una richiesta HTTP GET, [L] segue eventuali reindirizzamenti `3xx` e [D] stampa il contenuto e la intestazione della risposta su `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Scarica un file salvando l'[O]utput con lo stesso nome indicato nell'URL:

`curl {{[-O|--remote-name]}} {{https://example.com/nome_file.zip}}`

- Invia [d]ati form-encoded (con una richiesta POST di tipo `application/x-www-form-urlencoded`). Utilizza `--data @file_name` oppure `--data @'-'` per leggere da `stdin`:

`curl {{[-X|--request]}} POST {{[-d|--data]}} {{'name=mario'}} {{http://example.com/form}}`

- Invia una richiesta con una intestazione aggiuntiva utilizzando un metodo HTTP personalizzato attraverso un pro[x]y (come BurpSuite) ignorando i certificati autofirmati non sicuri:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} {{'Authorization: Bearer token'}} {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Invia dati in formato JSON, specificando la [H] intestazione content-type appropriata:

`curl {{[-d|--data]}} {{'{"name":"mario"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Invia il certificato client e la chiave per una risorsa omettendo la validazione del certificato:

`curl {{[-E|--cert]}} {{cliente.pem}} --key {{chiave.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Risolve un hostname con un indirizzo IP personalizzato con un output [v] dettagliato (simile alla modifica del file `/etc/hosts` per la risoluzione di un DNS personalizzato):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
