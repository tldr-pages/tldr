# grim

> Obtiene imágenes (capturas de pantalla) de un compositor Wayland.
> Más información: <https://sr.ht/~emersion/grim>.

- Hace una captura de pantalla:

`grim`

- Captura de pantalla a un archivo específico:

`grim -o {{ruta/al/archivo_resultado}}`

- Captura de Pantalla de una región específica:

`grim -g "{{<x_position>,<y_position> <width>x<height>}}"`

- Selecciona una región específica y toma una captura esa porción, (usando slurp):

`grim -g "{{$(slurp)}}"`

- Utiliza un nombre de archivo personalizado:

`grim "{{ruta/al/archivo.png}}"`

- Captura de Pantalla y la copia al portapapeles:

`grim - | {{clipboard_manager}}`
