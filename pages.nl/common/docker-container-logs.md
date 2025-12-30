# docker container logs

> Toon container logs.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Toon logs van een container:

`docker {{[logs|container logs]}} {{container_naam}}`

- Toon logs en volg:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{container_naam}}`

- Toon de laatste 5 regels:

`docker {{[logs|container logs]}} {{container_naam}} {{[-n|--tail]}} 5`

- Toon logs en voorzien van timestamps:

`docker {{[logs|container logs]}} {{[-t|--timestamps]}} {{container_naam}}`

- Toon logs vanaf een bepaald tijdstip van de uitvoering van de container (bijv. 23m, 10s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{container_naam}} --until {{time}}`
