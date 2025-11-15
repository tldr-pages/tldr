# gdown

> Descarga archivos desde Google Drive y otras URLs.
> Más información: <https://github.com/wkentaro/gdown>.

- Descarga un archivo desde una URL:

`gdown {{url}}`

- Descarga usando un ID de archivo:

`gdown {{id_de_archivo}}`

- Descarga con extracción de ID de archivo difuso (también funciona con enlaces <https://docs.google.com>):

`gdown --fuzzy {{url}}`

- Descarga una carpeta utilizando su ID o la URL completa:

`gdown {{id_de_carpeta|url}} -O {{ruta/a/directorio_de_salida}} --folder`

- Descarga un archivo tar, escríbelo en `stdout` y extráelo:

`gdown {{tar_url}} -O - --quiet | tar xvf -`
