# systemctl

> Controla el gestor de sistemas y servicios systemd.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Muestra todos los servicios en ejecución:

`systemctl status`

- Lista las unidades fallidas:

`systemctl --failed`

- Inicia, para, reinicia, recarga o muestra el estado de una unidad:

`systemctl {{start|stop|restart|reload|status}} {{unidad}}`

- Habilita o deshabilita una unidad para iniciarla al arrancar:

`systemctl {{enable|disable}} {{unidad}}`

- Reinicia systemd, lee unidades nuevas o modificadas:

`systemctl daemon-reload`

- Checa si una unidad está activa, habilitada, o en estado fallido:

`systemctl {{is-active|is-enabled|is-failed}} {{unidad}}`

- Lista todos los servicios, sockets, unidades auto-montadas filtradas por estado en ejecución o fallido:

`systemctl list-units {{[-t|--type]}} {{service|socket|automount}} --state {{failed|running}}`

- Muestra los contenidos y la ruta absoluta del archivo de una unidad:

`systemctl cat {{unidad}}`
