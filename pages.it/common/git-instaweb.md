# git instaweb

> Helper per avviare un server gitweb.
> Maggiori informazioni: <https://git-scm.com/docs/git-instaweb>.

- Avvia un server gitweb dal repository corrente:

`git instaweb --start`

- Resta in ascolto solo su localhost:

`git instaweb --start --local`

- Resta in ascolto su una porta specifica:

`git instaweb --start --port {{1234}}`

- Usa un HTTP daemon specifico:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Avvia automaticamente anche un web browser:

`git instaweb --start --browser`

- Interrompi il server gitweb in esecuzione:

`git instaweb --stop`

- Riavvia il server gitweb in esecuzione:

`git instaweb --restart`
