# docker volume

> Gestiona volúmenes de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/volume/>.

- Crea un volumen:

`docker volume create {{nombre_volumen}}`

- Crea un volumen con una etiqueta específica:

`docker volume create --label {{etiqueta}} {{nombre_volumen}}`

- Crea un volumen `tmpfs` con tamaño de 100 MiB y uid 1000:

`docker volume create {{[-o|--opt]}} {{type}}={{tmpfs}} {{[-o|--opt]}} {{device}}={{tmpfs}} {{[-o|--opt]}} {{o}}={{size=100m,uid=1000}} {{nombre_volumen}}`

- Lista todos los volúmenes:

`docker volume ls`

- Elimina un volumen:

`docker volume rm {{nombre_volumen}}`
