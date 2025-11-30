# podman image

> Gestiona imágenes Podman.
> Vea también: `podman build`, `podman import` y `podman pull`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imágenes locales de Podman:

`podman image {{[ls|list]}}`

- Elimina imágenes locales de Podman no utilizadas:

`podman image prune`

- Elimina todas las imágenes no utilizadas (no sólo aquellas sin una etiqueta):

`podman image prune {{[-a|--all]}}`

- Muestra la historia de una imagen Podman local:

`podman image history {{imagen}}`
