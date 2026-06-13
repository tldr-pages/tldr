# docker container logs

> Imprime registros del contenedor.
> Más información: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Imprime registros de un contenedor:

`docker {{[logs|container logs]}} {{nombre_contenedor}}`

- Imprime registros y los sigue:

`docker {{[logs|container logs]}} {{nombre_contenedor}} {{[-f|--follow]}}`

- Imprime las últimas 5 líneas:

`docker {{[logs|container logs]}} {{nombre_contenedor}} {{[-n|--tail]}} 5`

- Imprime registros y los añade con marcas de tiempo:

`docker {{[logs|container logs]}} {{nombre_contenedor}} {{[-t|--timestamps]}}`

- Imprime registros desde un momento determinado de la ejecución del contenedor (por ejemplo, 23m, 10s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{nombre_contenedor}} --until {{hora}}`
