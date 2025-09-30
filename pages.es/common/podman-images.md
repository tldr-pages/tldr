# podman images

> Gestiona imágenes de Podman.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas las imágenes de Podman:

`podman images`

- Lista todas las imágenes Podman incluyendo intermedias:

`podman images --all`

- Lista en modo silencioso (sólo ID numérico):

`podman images --quiet`

- Lista todas las imágenes Podman no utilizadas por ningún contenedor:

`podman images --filter dangling=true`

- Lista las imágenes que contienen una subcadena en su nombre:

`podman images "{{*imagen|imagen*}}"`
