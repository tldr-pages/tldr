# docker compose logs

> Muestra la salida de los contenedores en una aplicación Docker Compose.
> Más información: <https://docs.docker.com/reference/cli/docker/compose/logs/>.

- Muestra los logs de todos los servicios:

`docker compose logs`

- Muestra los logs de un servicio específico:

`docker compose logs {{nombre_servicio}}`

- Muestra los logs y sigue la salida nueva (como `tail --follow`):

`docker compose logs {{[-f|--follow]}}`

- Muestra los logs con marcas de tiempo:

`docker compose logs {{[-t|--timestamps]}}`

- Muestra solo las últimas `n` líneas de logs por contenedor:

`docker compose logs {{[-n|--tail]}} {{n}}`

- Muestra los logs desde un momento específico en adelante:

`docker compose logs --since {{marca_de_tiempo}}`

- Muestra los logs hasta un momento específico:

`docker compose logs --until {{marca_de_tiempo}}`
