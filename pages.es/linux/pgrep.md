# pgrep

> Busca o envía señales a procesos por su nombre.
> Vea también: `pidof`.
> Más información: <https://manned.org/pgrep>.

- Devuelve los PID de cualquier proceso en ejecución con una cadena de comando coincidente:

`pgrep {{nombre_del_proceso}}`

- También muestra el comando completo:

`pgrep {{[-a|--list-full]}} {{nombre_del_proceso}}`

- Busca procesos incluyendo sus opciones de línea de comandos:

`pgrep {{[-f|--full]}} "{{nombre_del_proceso}} {{parámetro}}"`

- Busca procesos ejecutados por un usuario específico:

`pgrep {{[-u|--euid]}} {{nombre_de_usuario}} {{nombre_del_proceso}}`
