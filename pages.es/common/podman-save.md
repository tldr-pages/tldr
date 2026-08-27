# podman save

> Guarda una imagen en un archivo o directorio local.
> Vea también: `podman load`, `podman export`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-save.1.html>.

- Guarda una imagen en un archivo `.tar`:

`podman save {{[-o|--output]}} {{ruta/al/archivo.tar}} {{image:tag}}`

- Guarda una imagen en `stdout`:

`podman save {{image:tag}} > {{ruta/al/archivo.tar}}`

- Guardar una imagen con compresión:

`podman save {{image:tag}} | {{[gzip|bzip2|xz|zstd|zstdchunked]}} > {{ruta/al/archivo.tar[.gz|.bz2|.xz|.zst|.zst]}}`

- Transfiere una imagen a un sistema remoto con compresión sobre la marcha y barra de progreso:

`podman save {{image:tag}} | zstd {{[-T|--threads]}} 0 --ultra | pv | ssh {{nombre_de_usuario}}@{{host_remoto}} podman load`
