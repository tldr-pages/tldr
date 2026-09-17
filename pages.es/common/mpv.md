# mpv

> Reproductor de audio/vídeo basado en MPlayer.
> Vea también: `mplayer`, `vlc`.
> Más información: <https://mpv.io/manual/stable/>.

- Reproduce un vídeo o audio desde una URL o un archivo:

`mpv {{url|ruta/al/archivo}}`

- Avanza o retrocede 5 segundos:

`{{<ArrowLeft>|<ArrowRight>}}`

- Avanzar o retroceder 1 minuto:

`{{<ArrowLeft>|<ArrowRight>}}`

- Disminuye o aumenta la velocidad de reproducción en un 10 %:

`{{<[>|<]>}}`

- Añade subtítulos desde un archivo:

`mpv --sub-file={{ruta/al/archivo}}`

- Hace una captura de pantalla del fotograma actual (guardada en `mpv-shotNNNN.jpg` por defecto):

`<s>`

- Reproduce un archivo a una velocidad específica (1 por defecto):

`mpv --speed {{0.01..100}} {{ruta/al/archivo}}`

- Reproduce un archivo utilizando un perfil definido en el archivo `mpv.conf`:

`mpv --profile {{nombre_del_perfil}} {{ruta/al/archivo}}`
