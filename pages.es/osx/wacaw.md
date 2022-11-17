# wacaw

> Herramienta de línea de comandos para macOS para capturar imágenes fijas y videos desde una cámara adjunta.
> Más información: <http://webcam-tools.sourceforge.net>.

- Toma una foto desde la cámara web:

`wacaw {{filename}}`

- Graba un video:

`wacaw --video {{filename}} --duration {{duration_in_seconds}}`

- Toma una foto con resolución personalizada:

`wacaw --width {{width}} --height {{height}} {{filename}}`

- Copia imagen recién tomada al portapapeles:

`wacaw --to-clipboard`

- Lista de los dispositivos disponibles:

`wacaw --list-devices`
