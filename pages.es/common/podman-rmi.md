# podman rmi

> Elimina imágenes de Podman.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Elimina una o más imágenes dados sus nombres:

`podman rmi {{imagen:tag imagen2:tag ...}}`

- Fuerza eliminar una imagen:

`podman rmi {{[-f|--force]}} {{imagen}}`

- Quita una imagen sin eliminar padres sin etiquetar:

`podman rmi --no-prune {{imagen}}`

- Muestra la ayuda:

`podman rmi {{[-h|--help]}}`
