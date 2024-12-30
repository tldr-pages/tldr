# noti

> Monitorea un proceso y activa una notificación gráfica de voz o servicio.
> Más información: <https://github.com/variadico/noti>.

- Muestra una notificación cuando `tar` termina de comprimir archivos:

`noti {{tar -cjf ejemplo.tar.bz2 ejemplo/}}`

- Muestra una notificación incluso cuando se pone después del comando a vigilar:

`{{comando_a_vigilar}}; noti`

- Monitorea un proceso por PID y activa una notificación cuando el PID desaparece:

`noti -w {{identificador_del_proceso}}`
