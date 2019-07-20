# docker-compose

> Esegui e gestisci applicazioni Docker composte da più container.
> Maggiori informazioni: <https://docs.docker.com/compose/reference/overview/>.

- Crea ed avvia tutti i container in background utilizzando il file `docker-compose.yml` nella directory corrente:

`docker-compose up -d`

- Avvia tutti i container, buildandoli di nuovo se necessario:

`docker-compose up --build`

- Avvia tutti i container utilizzando un file compose alternativo:

`docker-compose --file {{percorso/a/file}} up`

- Ferma tutti i container in esecuzione:

`docker-compose stop`

- Ferma e rimuovi tutti i container, reti, immagini e volumi:

`docker-compose down`

- Segui i log di tutti i container:

`docker-compose logs --follow`
