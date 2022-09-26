# docker-slim

> Analysiere und optimiere Docker Images.
> Weitere Informationen: <https://github.com/docker-slim/docker-slim>.

- Starte DockerSlim im interaktiven Modus:

`docker-slim`

- Analysiere die Docker Layer eines bestimmten Images:

`docker-slim xray --target {{image:tag}}`

- Linte ein Dockerfile:

`docker-slim lint --target {{pfad/zum/Dockerfile}}`

- Analysiere und generiere ein optimiertes Docker Image:

`docker-slim build {{image:tag}}`

- Zeige Hilfe für einen Unterbefehl:

`docker-slim {{unterbefehl}} --help`
