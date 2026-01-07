# docker image ls

> Gestisci immagini Docker.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Elenca tutte le immagini Docker:

`docker {{[images|image ls]}}`

- Elenca tutte le immagini Docker incluse quelle intermedie:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Elenca in modalità silenziosa (solo gli ID numerici):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Elenca tutte le immagini Docker che non sono usate da alcun container:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`
