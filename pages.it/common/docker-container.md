# docker container

> Gestisci container Docker.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/container/>.

- Elenca i container Docker attualmente in esecuzione:

`docker {{[ps|container ls]}}`

- Avvia uno o più container fermi:

`docker {{[start|container start]}} {{nome_container1}} {{nome_container2}}`

- Termina uno o più container in esecuzione:

`docker {{[kill|container kill]}} {{nome_container}}`

- Ferma uno o più container in esecuzione:

`docker {{[stop|container stop]}} {{nome_container}}`

- Sospendi tutti i processi dentro uno o più container:

`docker {{[pause|container pause]}} {{nome_container}}`

- Mostra informazioni dettagliate su uno o più container:

`docker container inspect {{nome_container}}`

- Esporta il filesystem di un container come archivio `.tar`:

`docker {{[export|container export]}} {{nome_container}}`

- Crea una nuova immagine dai cambiamenti di un container:

`docker {{[commit|container commit]}} {{nome_container}}`
