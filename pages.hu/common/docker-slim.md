# docker-slim

> Docker-képek elemzése és optimalizálása. További információ: <https://github.com/docker-slim/docker-slim>.

- Indítsa el a DockerSlim-et interaktív módban:

`docker-slim`

- Docker rétegek elemzése egy adott képből:

`docker-slim xray --target {{image:tag}}`

- Dockerfájl foltozása:

`docker-slim lint --target {{path/to/Dockerfile}}`

- Elemezzen és generáljon optimalizált Docker-képet:

`docker-slim build {{image:tag}}`

- Súgó megjelenítése egy alparancshoz:

`docker-slim {{subcommand}} --help`
