# docker

> Gestisci container ed immagini Docker.
> Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Elenca i container Docker attualmente in esecuzione:

`docker ps`

- Elenca tutti i container Docker (in esecuzione e arrestati):

`docker ps -a`

- Avvia un container da una immagine, con un nome personalizzato:

`docker run --name {{nome_container}} {{immagine}}`

- Avvia o arresta un container esistente:

`docker {{start|stop}} {{nome_container}}`

- Scarica (pull) un'immagine dal Docker registry:

`docker pull {{image}}`

- Avvia una shell all'interno di un container in esecuzione:

`docker exec -it {{nome_container}} {{sh}}`

- Rimuovi un container arrestato:

`docker rm {{nome_container}}`

- Ottieni e visualizza i log di un container:

`docker logs -f {{nome_container}}`
