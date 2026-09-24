# service

> Gestiona los servicios mediante la ejecución de scripts init.
> Se debe omitir la ruta completa del script (se asume `/etc/init.d/`).
> Más información: <https://manned.org/service>.

- Lista el nombre y el estado de todos los servicios:

`service --status-all`

- Inicia/Para/Reinicia/Recarga servicio (start/stop debería estar siempre disponible):

`service {{nombre_de_servicio}} {{start|stop|restart|reload}}`

- Hace un reinicio completo (ejecuta el script dos veces con start y stop):

`service {{nombre_de_servicio}} --full-restart`

- Muestra el estado actual de un servicio:

`service {{nombre_de_servicio}} status`
