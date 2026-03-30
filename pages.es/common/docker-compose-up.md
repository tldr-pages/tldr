# docker compose up

> Inicia y ejecuta los servicios de Docker definidos en un archivo Compose.
> Más información: <https://docs.docker.com/reference/cli/docker/compose/up/>.

- Inicia todos los servicios definidos en el archivo docker-compose:

`docker compose up`

- Inicia los servicios en segundo plano (modo desconectado):

`docker compose up {{[-d|--detach]}}`

- Inicia los servicios y reconstruye las imágenes antes de iniciar:

`docker compose up --build`

- Inicia solo servicios específicos:

`docker compose up {{servicio1 servicio2 ...}}`

- Inicia los servicios con un archivo compose personalizado:

`docker compose {{[-f|--file]}} {{ruta/a/config}} up`

- Inicia los servicios y elimina contenedores huérfanos:

`docker compose up --remove-orphans`

- Inicia los servicios con instancias escaladas:

`docker compose up --scale {{servicio}}={{cantidad}}`
