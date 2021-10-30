# systemctl

> Controla el sistema systemd y el gestor de servicios.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Mostrar todos los servicios en ejecución:

`systemctl status`

- Listar las unidades fallidas:

`systemctl --failed`

- Iniciar/Parar/Reiniciar/Recargar un servicio:

`systemctl {{start|stop|restart|reload}} {{unidad}}`

- Mostrar el estado de una unidad:

`systemctl status {{unidad}}`

- Habilitar/Deshabilitar una unidad para que se inicie en el arranque:

`systemctl {{enable/disable}} {{unidad}}`

- Enmascarar/Desenmascarar una unidad para evitar su habilitación y activación manual::

`systemctl {{mask|unmask}} {{unidad}}`

- Recargar systemd, buscando unidades nuevas o modificadas:

`systemctl daemon-reload`

- Comprobar si una unidad está habilitada:

`systemctl is-enabled {{unidad}}`
