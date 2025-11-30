# podman

> Herramienta de gestión sencilla para pods, contenedores e imágenes.
> Podman proporciona una línea de comando comparable con Docker-CLI. En pocas palabras: `alias docker=podman`.
> Más información: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Lista todos los contenedores (ambos en funcionamiento y detenidos):

`podman ps {{[-a|--all]}}`

- Crea un contenedor desde una imagen con un nombre personalizado:

`podman run --name {{nombre_del_contenedor}} {{imagen}}`

- Inicia o detiene un contenedor existente:

`podman {{start|stop}} {{nombre_del_contenedor}}`

- Extrae una imagen de un registro (Docker Hub predeterminado):

`podman pull {{imagen}}`

- Muestra la lista de imágenes ya descargadas:

`podman images`

- Abre una interfaz de comando dentro de un contenedor ya en funcionamiento:

`podman exec {{[-it|--interactive --tty]}} {{nombre_del_contenedor}} {{sh}}`

- Quita un contenedor detenido:

`podman rm {{nombre_del_contenedor}}`

- Muestra los registros de uno o más contenedores y muestra el registro (log):

`podman exec {{[-f|--follow]}} {{nombre_del_contenedor}} {{id_contenedor}}`
