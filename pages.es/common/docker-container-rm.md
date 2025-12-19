# docker container rm

> Elimina contenedores.
> Más información: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Elimina contenedores:

`docker {{[rm|container rm]}} {{contenedor1 contenedor2 ...}}`

- Elimina un contenedor de forma forzada:

`docker {{[rm|container rm]}} {{[-f|--force]}} {{contenedor1 contenedor2 ...}}`

- Elimina un contenedor y sus volúmenes:

`docker {{[rm|container rm]}} {{[-v|--volumes]}} {{contenedor}}`

- Muestra la ayuda:

`docker {{[rm|container rm]}} {{[-h|--help]}}`
