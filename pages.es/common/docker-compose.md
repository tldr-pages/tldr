# docker compose

> Ejecuta y gestiona aplicaciones Docker multicontenedor.
> Más información: <https://docs.docker.com/compose/reference/>.

- Lista todos los contenedores en ejecución:

`docker compose ps`

- Crea e inicia todos los contenedores en segundo plano usando un archivo `docker-compose.yml` desde el directorio actual:

`docker compose up --detach`

- Inicia todos los contenedores, y se reconstruye si es necesario:

`docker compose up --build`

- Inicia todos los contenedores especificando un nombre de proyecto y utilizando un archivo de composición alternativo:

`docker compose -p {{nombre_proyecto}} --file {{ruta/al/archivo}} up`

- Detiene todos los contenedores en ejecución:

`docker compose stop`

- Detiene y elimina todos los contenedores, redes, imágenes y volúmenes:

`docker compose down --rmi all --volumes`

- Sigue los registros de todos los contenedores:

`docker compose logs --follow`

- Sigue los registros de un contenedor específico:

`docker compose logs --follow {{nombre_del_contenedor}}`
