# docker container logs

> Imprime registros del contenedor.
> Más información: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Imprime registros de un contenedor:

`docker {{[logs|container logs]}} {{nombre_contenedor}}`

- Imprime registros y los sigue:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{nombre_contenedor}}`

- Imprime las últimas 5 líneas:

`docker {{[logs|container logs]}} {{nombre_contenedor}} {{[-n|--tail]}} 5`

- Imprime registros y los añade con marcas de tiempo:

`docker {{[logs|container logs]}} {{[-t|--timestamps]}} {{nombre_contenedor}}`

- Imprime registros desde un momento determinado de la ejecución del contenedor (por ejemplo, 23 m, 10 s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{nombre_contenedor}} --until {{hora}}`
