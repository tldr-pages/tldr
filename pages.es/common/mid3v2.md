# mid3v2

> Edita etiquetas de audio.
> Vea también: `id3v2`.
> Más información: <https://mutagen.readthedocs.io/en/latest/man/mid3v2.html>.

- Lista de todos los marcos ID3v2.3 o ID3v2.4 admitidos y sus significados:

`id3v2 --list-frames {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`

- Lista de todos los géneros numéricos ID3v1 admitidos:

`id3v2 --list-genres {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`

- Lista todas las etiquetas en archivos específicos:

`id3v2 --list {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`

- Establece información específica sobre artistas, álbumes o canciones:

`id3v2 {{--artist|--album|--song}}={{string}} {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`

- Establece información específica de la imagen:

`id3v2 --picture={{filename:description:image_type:mime_type}} {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`

- Establece información específica del año:

`id3v2 --year={{YYYY}} {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`

- Establece información de fecha específica:

`id3v2 --date={{YYYY-MM-DD}} {{ruta/al/archivo1.mp3 ruta/al/archivo2.mp3 ...}}`
