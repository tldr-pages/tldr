# docker container run

> Ejecuta un comando en un nuevo contenedor Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Ejecuta un comando en un nuevo contenedor desde una imagen etiquetada:

`docker {{[run|container run]}} {{image:tag}} {{comando}}`

- Ejecuta un comando en un nuevo contenedor en segundo plano y muestra su ID:

`docker {{[run|container run]}} {{[-d|--detach]}} {{imagen}} {{comando}}`

- Ejecuta un comando en un contenedor único en modo interactivo y pseudo-TTY:

`docker {{[run|container run]}} --rm {{[-it|--interactive --tty]}} {{imagen}} {{comando}}`

- Ejecuta el comando en un nuevo contenedor con las variables de entorno pasadas:

`docker {{[run|container run]}} {{[-e|--env]}} '{{variable}}={{value}}' {{[-e|--env]}} {{variable}} {{imagen}} {{comando}}`

- Ejecuta comando en un nuevo contenedor con volúmenes montados vinculados:

`docker {{[run|container run]}} {{[-v|--volume]}} /{{ruta/a/host_path}}:/{{ruta/a/ruta_contenedor}} {{imagen}} {{comando}}`

- Ejecuta comando en un nuevo contenedor con puertos publicados:

`docker {{[run|container run]}} {{[-p|--publish]}} {{puerto_host}}:{{puerto_contenedor}} {{imagen}} {{comando}}`

- Ejecuta comando en un nuevo contenedor sobrescribiendo el punto de entrada de la imagen:

`docker {{[run|container run]}} --entrypoint {{comando}} {{imagen}}`

- Ejecuta comando en un nuevo contenedor conectándolo a una red:

`docker {{[run|container run]}} --network {{red}} {{imagen}}`
