# docker compose

> Ejecuta y gestiona múltiples contenedores Docker.
> Más información: <https://docs.docker.com/compose/reference/>.

- Lista los contenedores en ejecución:

`docker compose ps`

- Crea e inicia todos los contenedores en segundo plano usando el archivo `docker-compose.yml` en el directorio actual:

`docker compose up --detach`

- Inicia todos los contenedores y reconstruye si es ncesario:

`docker compose up --build`

- Inicia todos los contenedores especificando un nombre de proyecto y usando un archivo compose alternativo:

`docker compose  -p {{nombre_de_proyecto}} --file {{ruta/al/directorio}} up`

- Detiene todos los contenedores en ejecución:

`docker compose stop`

- Detiene y elimina todos los contenedores, redes, imágenes y volúmenes:

`docker compose down --rmi all --volumes`

- Sigue los registros de todos los contenedores:

`docker compose logs --follow`

- Sigue los registros de un contenedor específico:

`docker compose logs --follow {{nombre_de_contenedor}}`
