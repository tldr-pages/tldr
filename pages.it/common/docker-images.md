# docker images

> Gestisci immagini Docker.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Elenca tutte le immagini Docker:

`docker images`

- Elenca tutte le immagini Docker incluse quelle intermedie:

`docker images {{[-a|--all]}}`

- Elenca in modalità silenziosa (solo gli ID numerici):

`docker images {{[-q|--quiet]}}`

- Elenca tutte le immagini Docker che non sono usate da alcun container:

`docker images {{[-f|--filter]}} dangling=true`
