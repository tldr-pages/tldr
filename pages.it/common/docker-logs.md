# docker logs

> Mostra i log di un container.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Mostra i log di un container:

`docker logs {{nome_container}}`

- Segui i log di un container:

`docker logs {{[-f|--follow]}} {{nome_container}}`

- Mostra le ultime 5 righe:

`docker logs {{nome_container}} {{[-n|--tail]}} {{5}}`

- Mostra i log mettendo un timestamp in coda:

`docker logs {{[-t|--timestamps]}} {{nome_container}}`

- Mostra i log avvenuti prima di un dato momento nell'esecuzione del container (ad esempio, 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{nome_container}} --until {{momento}}`
