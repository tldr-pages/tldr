# docker

> Administra contenedores e imágenes de Docker.
> Más información: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Lista los contenedores de Docker en ejecución:

`docker ps`

- Lista todos los contenedores de Docker (en ejecución y detenidos):

`docker ps -a`

- Inicia un contenedor desde una imagen con un nombre personalizado:

`docker run --name {{nombre_contenedor_personalizado}} {{imagen}}`

- Inicia o detiene un contenedor existente:

`docker {{start|stop}} {{nombre_contenedor}}`

- Extraer una imagen de un registro de Docker:

`docker pull {{imagen}}`

- Inicia una shell dentro de un contenedor en ejecución:

`docker exec -it {{nombre_contenedor}} {{sh}}`

- Elimina un contenedor detenido:

`docker rm {{nombre_contenedor}}`

- Busca y sigue los registros de un contenedor:

`docker logs -f {{nombre_contenedor}}`
