# journalctl

> Consulta el registro systemd.
> Más información: <https://manned.org/journalctl>.

- Muestra todos los mensajes con nivel de prioridad 3 (errores) de este [b]oot:

`journalctl -b --priority=3`

- Elimina los registros diarios con más de 2 días de antigüedad:

`journalctl --vacuum-time=2d`

- Muestra solo las últimas N líneas y sigue los mensajes nuevos (como `tail -f` de un syslog tradicional):

`journalctl --lines {{N}} --follow`

- Muestra todos los mensajes de una [u]nidad específica:

`journalctl --unit {{unidad}}`

- Muestra los registros de una unidad determinada desde la última vez que se inició:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unidad}})`

- Filtra mensajes dentro de un intervalo de tiempo (marca de tiempo o marcadores de posición como "ayer"):

`journalctl --since {{now|today|yesterday|tomorrow}} --until "{{YYYY-MM-DD HH:MM:SS}}"`

- Muestra todos los mensajes de un proceso específico:

`journalctl _PID={{pid}}`

- Mostrar todos los mensajes de un ejecutable específico:

`journalctl {{ruta/al/ejecutable}}`
