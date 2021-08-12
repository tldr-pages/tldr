# docker image

> Gestionare imagini Docker.
> A se vedea, de asemenea, `docker build`, `docker import', si `docher trage`.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/image/>

- Listează imaginile Docker locale:

`docker image ls`

- Ștergeți imaginile Docker locale neutilizate:

`docker image prune`

- Ștergeți toate imaginile neutilizate (nu doar cele fără etichetă):

`docker image prune --all`

- Afișează istoricul unei imagini locale Docker:

`docker image history {{image}}`
