# podman-compose

> Ejecuta y gestiona la definición del contenedor según la especificación de composición (Compose Specification).
> Más información: <https://github.com/containers/podman-compose>.

- Lista todos los contenedores en funcionamiento:

`podman-compose ps`

- Crea e inicia todos los contenedores en segundo plano utilizando un `docker-compose.yml` local:

`podman-compose up -d`

- Inicia todos los contenedores, construyendo si es necesario:

`podman-compose up --build`

- Inicia todos los contenedores usando un archivo de composición alterno:

`podman-compose {{[-f|--file]}} {{ruta/al/archivo.yaml}} up`

- Detiene todos los contenedores en funcionamiento:

`podman-compose stop`

- Quita todos los contenedores, redes y volúmenes:

`podman-compose down --volumes`

- Sigue los registros de un contenedor (omite todos los nombres de los contenedores):

`podman-compose logs --follow {{nombre_del_contenedor}}`

- Ejecuta un comando de una sola vez en un servicio sin puertos mapeados:

`podman-compose run {{nombre_del_servicio}} {{comando}}`
