# grim

> Obtiene imágenes (capturas de pantalla) de un compositor Wayland.
> Más información: <https://sr.ht/~emersion/grim>.

- Hace una captura de pantalla:

`grim`

- Captura de pantalla a un archivo específico:

`grim -o {{ruta/al/archivo_resultado}}`

- Captura de pantalla de una región específica:

`grim -g "{{posición_x}},{{posición_y}} {{ancho}}x{{alto}}"`

- Selecciona una región específica y toma una captura de dicha porción, usando slurp:

`grim -g "{{$(slurp)}}"`

- Utiliza un nombre de archivo personalizado:

`grim "{{ruta/al/archivo.png}}"`

- Captura de pantalla y la copia al portapapeles:

`grim - | {{clipboard_manager}}`
