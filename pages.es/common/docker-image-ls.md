# docker image ls

> Muestra una lista de imágenes de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Muestra una lista de todas las imágenes de Docker:

`docker {{[images|image ls]}}`

- Muestra una lista de todas las imágenes de Docker, incluidas las intermedias:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Muestra la salida en modo silencioso (solo ID numéricos):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Muestra todas las imágenes de Docker que no utiliza ningún contenedor:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Muestra las imágenes que contengan una subcadena en su nombre:

`docker {{[images|image ls]}} "{{*nombre*}}"`

- Ordena las imágenes por tamaño:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
