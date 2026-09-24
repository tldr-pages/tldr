# podman pull

> Descarga imágenes de un registro de contenedores.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-pull.1.html>.

- Descarga una imagen de contenedor específica:

`podman pull {{imagen}}:{{etiqueta}}`

- Descarga una imagen de contenedor en modo silencioso:

`podman pull {{[-q|--quiet]}} {{imagen}}:{{etiqueta}}`

- Descarga todas las etiquetas de una imagen de contenedor:

`podman pull {{[-a|--all-tags]}} {{imagen}}`

- Descarga una imagen de contenedor para una plataforma específica:

`podman pull --platform {{linux/arm64}} {{imagen}}:{{etiqueta}}`

- Descarga una imagen de contenedor sin verificación TLS:

`podman pull --tls-verify=false {{imagen}}:{{etiqueta}}`

- Muestra la ayuda:

`podman pull {{[-h|--help]}}`
