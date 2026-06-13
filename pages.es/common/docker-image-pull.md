# docker image pull

> Descarga imágenes de Docker desde un registro.
> Más información: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Descarga una imagen de Docker específica:

`docker {{[pull|image pull]}} {{imagen}}:{{etiqueta}}`

- Descarga una imagen de Docker específica en modo silencioso:

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{imagen}}:{{etiqueta}}`

- Descarga todas las etiquetas de una imagen de Docker específica:

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{imagen}}`

- Descarga imágenes de Docker para una plataforma específica:

`docker {{[pull|image pull]}} --platform {{linux/amd64}} {{imagen}}:{{etiqueta}}`

- Muestra la ayuda:

`docker {{[pull|image pull]}} --help`
