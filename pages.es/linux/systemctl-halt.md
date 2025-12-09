# systemctl-halt

> Apaga y detiene el sistema (detiene el kernel del SO pero mantiene el hardware encendido).
> Vea también: `halt`.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#halt>.

- Detiene el sistema:

`systemctl halt`

- Detiene el sistema inmediatamente sin solicitar a los servicios que se detengan elegantemente:

`systemctl halt --force`

- Detiene el sistema inmediatamente sin enviar notificaciones a los usuarios conectados:

`systemctl halt --force --no-wall`

- Detiene el sistema inmediatamente sin terminar procesos o desmontar sistemas de archivos (peligroso, puede causar pérdida de datos):

`systemctl halt --force --force`

- Programa una detención a una hora específica (ej., 23:00):

`systemctl halt --when 23:00`

- Programa una detención después de cierta duración (ej., 2 horas):

`systemctl halt --when +2h`

- Cancela una detención programada:

`systemctl halt --when cancel`
