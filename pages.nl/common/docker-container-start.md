# docker container start

> Start gestopte containers.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Een Docker-container starten:

`docker {{[start|container start]}} {{container}}`

- Start een container, koppel `stdout` en `stderr` aan en stuur signalen door:

`docker {{[start|container start]}} {{[-a|--attach]}} {{container}}`

- Start een of meer containers:

`docker {{[start|container start]}} {{container1 container2 ...}}`

- Toon de help:

`docker {{[start|container start]}} --help`
