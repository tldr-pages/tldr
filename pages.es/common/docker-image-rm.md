# docker image rm

> Elimina imágenes de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Elimina una o más imágenes por sus nombres:

`docker {{[rmi|image rm]}} {{imagen1 imagen2 ...}}`

- Fuerza la eliminación de una imagen:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{imagen}}`

- Elimina una imagen sin borrar los padres sin etiqueta:

`docker {{[rmi|image rm]}} --no-prune {{imagen}}`

- Muestra la ayuda:

`docker {{[rmi|image rm]}} --help`
