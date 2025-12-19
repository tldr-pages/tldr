# docker rm

> Elimina contenedores.
> Más información: <https://docs.docker.com/reference/cli/docker/container/rm/>.

- Elimina los contenedores:

`docker rm {{contenedor1 contenedor2 ...}}`

- Elimina de manera forzada contenedores:

`docker rm {{[-f|--force]}} {{contenedor1 contenedor2 ...}}`

- Elimina un contenedor y sus volúmenes:

`docker rm {{[-v|--volumes]}} {{contenedor}}`

- Muestra la ayuda:

`docker rm {{[-h|--help]}}`
