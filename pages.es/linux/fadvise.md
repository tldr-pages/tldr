# fadvise

> Controla el comportamiento de la caché de archivos de Linux.
> Más información: <https://manned.org/fadvise>.

- Precarga un archivo en la caché:

`fadvise {{[-a|--advice]}} willneed {{ruta/al/archivo}}`

- Sugiere eliminar un archivo de la caché:

`fadvise {{ruta/al/archivo}}`

- Muestra la ayuda:

`fadvise --help`
