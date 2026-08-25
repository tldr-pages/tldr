# podman load

> Carga una imagen desde un archivo OCI o Docker creado con `podman save`.
> Vea también: `podman save`, `podman import`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-load.1.html>.

- Carga una imagen desde un archivo `.tar`:

`podman load {{[-i|--input]}} {{ruta/al/archivo.tar}}`

- Carga una imagen desde un archivo `.tar` comprimido:

`podman load {{[-i|--input]}} {{ruta/al/archivo.tar[.gz|.bz2|.xz|.zst]}}`

- Carga una imagen y muestra una salida silenciosa (solo muestra el ID de la imagen):

`podman load {{[-q|--quiet]}} {{[-i|--input]}} {{ruta/al/archivo.tar}}`

- Carga una imagen desde `stdin`:

`podman < {{ruta/al/archivo.tar}} load`
