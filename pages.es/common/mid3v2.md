# mid3v2

> Editar etiquetas de audio.
> Ver también: `id3v2`.
> Más información: <https://manned.org/mid3v2.1>.

- Lista de todos los marcos ID3v2.3 o ID3v2.4 admitidos y sus significados:

`id3v2 --list-frames {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`

- Lista de todos los géneros numéricos ID3v1 admitidos:

`id3v2 --list-genres {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`

- Lista todas las etiquetas en archivos específicos:

`id3v2 --list {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`

- Establece información específica sobre artistas, álbumes o canciones:

`id3v2 {{--artist|--album|--song}}={{string}} {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`

- Establece información específica de la imagen:

`id3v2 --picture={{filename:description:image_type:mime_type}} {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`

- Establece información específica del año:

`id3v2 --year={{YYYY}} {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`

- Establece información de fecha específica:

`id3v2 --date={{YYYY-MM-DD}} {{ruta/a/archivo1.mp3 ruta/a/archivo2.mp3 ...}}`
