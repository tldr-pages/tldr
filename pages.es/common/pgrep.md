# pgrep

> Encuentra o envía una señal a procesos por nombre.
> Más información: <https://www.manned.org/pgrep>.

- Regresa PIDs de cualquier proceso de ejecución con una cadena de comando que coincida:

`pgrep {{nombre_del_proceso}}`

- Busca procesos incluyendo sus opciones de línea de comandos:

`pgrep --full "{{nombre_del_proceso}} {{parámetro}}"`

- Busca procesos gestionados por un usuario específico:

`pgrep --euid root {{nombre_del_proceso}}`
