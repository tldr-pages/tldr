# podman run

> Ejecuta un comando en un nuevo contenedor Podman.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-run.1.html>.

- Ejecuta el comando en un nuevo contenedor de una imagen etiquetada:

`podman run {{imagen:tag}} {{comando}}`

- Ejecuta el comando en un nuevo contenedor en el fondo y muestra su ID:

`podman run {{[-d|--detach]}} {{imagen:tag}} {{comando}}`

- Ejecuta el comando en un contenedor único en modo interactivo y pseudo-TTY:

`podman run --rm {{-it|--interactive --tty}} {{imagen:tag}} {{comando}}`

- Ejecuta el comando en un nuevo contenedor con variables de entorno enviadas:

`podman run {{[-e|--env]}} '{{variable}}={{valor}}' {{[-e|--env]}} {{variable}} {{imagen:tag}} {{comando}}`

- Ejecuta el comando en un nuevo contenedor con volúmenes montados en un contenedor:

`podman run {{[-v|--volume]}} {{/ruta/a/ruta_del_host}}:{{/ruta/a/ruta_del_contenedor}} {{imagen:tag}} {{comando}}`

- Ejecuta comando en un nuevo contenedor con los puertos publicados:

`podman run {{[-p|--publish]}} {{puerto_del_anfitrion}}:{{puerto_del_contenedor}} {{imagen:tag}} {{comando}}`

- Ejecuta el comando en un nuevo contenedor sobrescribiendo el punto de entrada (entrypoint) de la imagen:

`podman run --entrypoint {{comando}} {{imagen:tag}}`

- Ejecuta el comando en un nuevo contenedor que lo conecta a una red:

`podman run --network {{red}} {{imagen:tag}}`
