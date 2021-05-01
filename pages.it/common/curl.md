# curl

> Trasferisci dati da o ad un server.
> Supporta molti protocollo, tra cui HTTP, FTP e POP3.
> Maggiori informazioni: <https://curl.se>.

- Scarica il contenuto di un URL in un file:

`curl {{http://example.com}} -o {{nome_file}}`

- Scarica un file, salvando l'output con lo stesso nome indicato nell'URL:

`curl -O {{http://example.com/nome_file}}`

- Scarica un file, seguendo reindirizzamenti, e continuando automaticamente (riprendendo) un trasferimento precedente:

`curl -O -L -C - {{http://example.com/nome_file}}`

- Invia dati form-encoded (richiesta POST di tipo `application/x-www-form-urlencoded`):

`curl -d {{'nome=mario'}} {{http://example.com/form}}`

- Invia una richiesta con un header aggiuntivo, utilizzando un metodo HTTP personalizzato:

`curl -H {{'X-Mio-Header: 123'}} -X {{PUT}} {{http://example.com}}`

- Invia dati in formato JSON, specificando l'header content-type appropriato:

`curl -d {{'{"nome":"mario"}'}} -H {{'Content-Type: application/json'}} {{http://example.com/utenti/1234}}`

- Utilizza un nome utente ed una password per l'autenticazione con il server:

`curl -u utente:password {{http://example.com}}`

- Utilizza un certificato ed una chiave per una risorsa, ignorando la validazione dei certificati:

`curl --cert {{client.pem}} --key {{chiave.pem}} --insecure {{https://example.com}}`
