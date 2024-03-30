# docker compose

> Esegui e gestisci applicazioni Docker composte da più container.
> Maggiori informazioni: <https://docs.docker.com/compose/reference/>.

- Elenca i container in esecuzione:

`docker compose ps`

- Crea ed avvia tutti i container in background utilizzando il file `docker-compose.yml` nella directory corrente:

`docker compose up --detach`

- Avvia tutti i container, buildandoli di nuovo se necessario:

`docker compose up --build`

- Avvia tutti i contenitori specificando un nome di progetto e utilizzando un file compose alternativo:

`docker compose -p {{nome_di_progetto}} --file {{percorso/del/file}} up`

- Ferma tutti i container in esecuzione:

`docker compose stop`

- Ferma e rimuovi tutti i container, reti, immagini e volumi:

`docker compose down --rmi all --volumes`

- Segui i log di tutti i container:

`docker compose logs --follow`

- Segui i log di un container specifico:

`docker compose logs --follow {{nome_container}}`
