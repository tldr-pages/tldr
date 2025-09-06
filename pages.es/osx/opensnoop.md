# opensnoop

> Herramienta que rastrea las aperturas de archivos en tu sistema.
> Más información: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- Imprime todos los archivos abiertos a medida que ocurren:

`sudo opensnoop`

- Rastrea todos los archivos abiertos por un proceso por su nombre:

`sudo opensnoop -n "{{nombre_proceso}}"`

- Rastrea todos los archivos abiertos por un proceso por PID:

`sudo opensnoop -p {{PID}}`

- Seguimiento de los procesos que abren un archivo especificado:

`sudo opensnoop -f {{ruta/al/archivo}}`
