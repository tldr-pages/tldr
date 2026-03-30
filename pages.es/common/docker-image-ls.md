# docker image ls

> Lista las imágenes de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Lista todas las imágenes de Docker:

`docker {{[images|image ls]}}`

- Lista todas las imágenes de Docker incluyendo las intermedias:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Muestra la salida en modo silencioso (solo IDs numéricos):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Lista todas las imágenes de Docker no usadas por ningún contenedor:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Lista las imágenes que contienen una subcadena en su nombre:

`docker {{[images|image ls]}} "{{*nombre*}}"`

- Ordena las imágenes por tamaño:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
