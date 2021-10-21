# docker-compose

> Ejecuta y gestiona múltiples contenedores Docker.
> Más información: <https://docs.docker.com/compose/reference/>.

- Lista los contenedores en ejecución:

`docker-compose ps`

- Crea e inicia todos los contenedores en segundo plano usando el archivo `docker-compose.yml` en el directorio actual:

`docker-compose up -d`

- Inicia todos los contenedores y reconstruye si es ncesario:

`docker-compose up --build`

- Inicia todos los contenedores usando un archivo compose alternativo:

`docker-compose --file {{ruta/al/directorio}} up`

- Detiene todos los contenedores en ejecución:

`docker-compose stop`

- Detiene y elimina todos los contenedores, redes, imágenes y volúmenes:

`docker-compose down --rmi all --volumes`

- Sigue los registros de todos los contenedores:

`docker-compose logs --follow`
