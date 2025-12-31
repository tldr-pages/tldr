# docker

> Gestisci container ed immagini Docker.
> Alcuni comandi aggiuntivi, come `run`, hanno la propria documentazione.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/>.

- Elenca tutti i container Docker (in esecuzione e arrestati):

`docker ps {{[-a|--all]}}`

- Avvia un container da una immagine, con un nome personalizzato:

`docker run --name {{nome_container}} {{immagine}}`

- Avvia o arresta un container esistente:

`docker {{start|stop}} {{nome_container}}`

- Scarica (pull) un'immagine dal Docker registry:

`docker pull {{image}}`

- Avvia una shell all'interno di un container in esecuzione:

`docker exec {{[-it|--interactive --tty]}} {{nome_container}} {{sh}}`

- Rimuovi un container arrestato:

`docker rm {{nome_container}}`

- Ottieni e visualizza i log di un container:

`docker logs {{[-f|--follow]}} {{nome_container}}`
