# trackfetch

> Descargar las canciones de un archivo de texto como archivos MP3, M4A u Opus con etiquetas, usando los metadatos de Spotify y el audio de YouTube.
> Requiere `yt-dlp`, `ffmpeg` y el identificador de cliente y el secreto de Spotify (archivo de configuración o `SPOTIFY_CLIENT_ID` y `SPOTIFY_CLIENT_SECRET`).
> Más información: <https://github.com/ByteMe6/trackfetch#usage>.

- Descargar todas las canciones de un archivo con una línea `Artista - Título` por canción en el directorio actual:

`trackfetch {{path/to/songs.txt}}`

- Descargar las canciones en un directorio concreto:

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Conservar el audio original de YouTube en lugar de convertirlo a MP3:

`trackfetch {{path/to/songs.txt}} {{[-f|--format]}} {{opus|m4a}}`

- Descargar algunas canciones sin archivo de texto:

`trackfetch {{"Artist - Title"}} {{"Another Artist - Another Title"}}`

- Nombrar los archivos solo con el título de la canción en lugar de `Artista - Título`:

`trackfetch {{path/to/songs.txt}} --title-only`

- Usar un archivo de configuración para los valores por defecto:

`trackfetch {{path/to/songs.txt}} {{[--config]}} {{path/to/config.ini}}`

- Esperar unos segundos entre canciones para no superar los límites de peticiones:

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Reintentar las canciones que fallaron en la ejecución anterior:

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt > {{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`
