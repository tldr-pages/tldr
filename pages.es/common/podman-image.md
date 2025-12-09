# podman image

> Gestiona imágenes Docker.
> Vea también: `podman build`, `podman import` y `podman pull`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imágenes locales de Docker:

`podman image ls`

- Elimina imágenes locales de Docker no utilizadas:

`podman image prune`

- Elimina todas las imágenes no utilizadas (no sólo aquellas sin una etiqueta):

`podman image prune --all`

- Muestra la historia de una imagen Docker local:

`podman image history {{imagen}}`
