# podman export

> Exporta el sistema de archivos de un contenedor y lo guarda como un archivo tar en el equipo local.
> Vea también: `podman import`, `podman save`.
> Más información: <https://docs.podman.io/en/latest/markdown/podman-export.1.html>.

- Exporta el sistema de archivos de un contenedor a un archivo `.tar`:

`podman export {{[-o|--output]}} {{ruta/al/archivo.tar}} {{nombre_o_id_del_contenedor}}`

- Exporta el sistema de archivos de un contenedor a `stdout`:

`podman export {{nombre_o_id_del_contenedor}} > {{ruta/al/archivo.tar}}`
