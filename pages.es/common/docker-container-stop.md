# docker container stop

> Detiene uno o varios contenedores en ejecución.
> Más información: <https://docs.docker.com/reference/cli/docker/container/stop/>.

- Detiene un contenedor de Docker:

`docker {{[stop|container stop]}} {{contenedor}}`

- Detiene un contenedor enviándole una señal específica:

`docker {{[stop|container stop]}} {{[-s|--signal]}} {{señal}} {{contenedor}}`

- Detiene un contenedor, esperando un número específico de segundos antes de forzar su cierre:

`docker {{[stop|container stop]}} {{[-t|--timeout]}} {{segundos}} {{contenedor}}`

- Detiene uno o varios contenedores:

`docker {{[stop|container stop]}} {{contenedor1 contenedor2 ...}}`

- Muestra la ayuda:

`docker {{[stop|container stop]}} --help`
