# podman image

> Gestiona imágenes OCI/Docker.
> Vea también: `podman build`, `podman import` y `podman pull`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imágenes locales de OCI/Docker:

`podman image {{[ls|list]}}`

- Elimina imágenes locales de OCI/Docker no utilizadas:

`podman image prune`

- Elimina todas las imágenes no utilizadas (no sólo aquellas sin una etiqueta):

`podman image prune {{[-a|--all]}}`

- Muestra la historia de una imagen OCI/Docker local:

`podman image history {{imagen}}`
