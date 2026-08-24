# docker

> Administra contenedores e imágenes de Docker.
> Algunos subcomandos, como `run`, tienen su propia documentación de uso.
> Más información: <https://docs.docker.com/reference/cli/docker/>.

- Lista todos los contenedores de Docker (en ejecución y detenidos):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Inicia un contenedor desde una imagen con un nombre personalizado:

`docker {{[run|container run]}} --name {{nombre_de_contenedor}} {{imagen}}`

- Inicia o detiene un contenedor existente:

`docker container {{start|stop}} {{nombre_de_contenedor}}`

- Descarga una imagen desde un registro de Docker:

`docker {{[pull|image pull]}} {{imagen}}`

- Muestra la lista de imágenes descargadas:

`docker {{[images|image ls]}}`

- Inicia una línea de comandos dentro de un contenedor en ejecución:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{nombre_de_contenedor}} {{sh}}`

- Elimina un contenedor detenido:

`docker {{[rm|container rm]}} {{nombre_de_contenedor}}`

- Obtén y sigue los registros de un contenedor:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{nombre_de_contenedor}}`
