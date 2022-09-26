# systemctl

> Controla el sistema systemd y el gestor de servicios.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Muestra todos los servicios en ejecución:

`systemctl status`

- Lista las unidades fallidas:

`systemctl --failed`

- Inicia/Para/Reinicia/Recarga un servicio:

`systemctl {{start|stop|restart|reload}} {{unidad}}`

- Muestra el estado de una unidad:

`systemctl status {{unidad}}`

- Habilita/Deshabilita una unidad para que se inicie en el arranque:

`systemctl {{enable/disable}} {{unidad}}`

- Enmascara/Desenmascara una unidad para evitar su habilitación y activación manual:

`systemctl {{mask|unmask}} {{unidad}}`

- Recarga systemd, buscando unidades nuevas o modificadas:

`systemctl daemon-reload`

- Comprueba si una unidad está habilitada:

`systemctl is-enabled {{unidad}}`
