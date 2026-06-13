# docker container start

> Inicia contenedores detenidos.
> Más información: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Inicia un contenedor Docker:

`docker {{[start|container start]}} {{contenedor}}`

- Inicia un contenedor, adjuntando `stdout` y `stderr` y reenviando señales:

`docker {{[start|container start]}} {{[-a|--attach]}} {{contenedor}}`

- Inicia uno o más contenedores:

`docker {{[start|container start]}} {{contenedor1 contenedor2 ...}}`

- Muestra la ayuda:

`docker {{[start|container start]}} --help`
