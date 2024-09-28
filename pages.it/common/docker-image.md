# docker image

> Gestisci immagini Docker.
> Vedi anche `docker build`, `docker import` e `docker pull`.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/image/>.

- Elenca tutte le immagini Docker locali:

`docker image ls`

- Elimina le immagini Docker locali inutilizzate:

`docker image prune`

- Cancella tutte le immagini inutilizzate (non solo quelle sprovviste di tag):

`docker image prune --all`

- Mostra la cronologia di un'immagine Docker locale:

`docker image history {{immagine}}`
