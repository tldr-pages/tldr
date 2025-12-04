# podman images

> Gestiona imágenes de contenedores OCI/Docker.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas las imágenes de contenedores:

`podman images`

- Lista todas las imágenes de contenedores incluyendo intermedias:

`podman images {{[-a|--all]}}`

- Lista en modo silencioso (sólo ID numérico):

`podman images {{[-q|--quiet]}}`

- Lista todas las imágenes no utilizadas por ningún contenedor:

`podman images {{[-f|--filter]}} dangling=true`

- Lista las imágenes que contienen una subcadena en su nombre:

`podman images "{{*imagen|imagen*}}"`
