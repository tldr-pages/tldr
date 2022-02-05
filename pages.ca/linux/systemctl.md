# systemctl

> Controla el sistema systemd i el gestor de serveis.
> Més informació: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Mostra tots els serveis en execució:

`systemctl status`

- Llista les unitats fallides:

`systemctl --failed`

- Inicia/Atura/Reinicia/Recarrega un servei:

`systemctl {{start|stop|restart|reload}} {{unitat}}`

- Mostra l'estat d'una unitat:

`systemctl status {{unitat}}`

- Habilita/Deshabilita una unitat perquè s'inicii en l'arrencada:

`systemctl {{enable|disable}} {{unitat}}`

- Enmascara/Desenmascara una unitat per evitar la seva habilitació i activació manual:

`systemctl {{mask|unmask}} {{unida`

- Recarrega systemd, buscant unitats noves o modificades:

`systemctl daemon-reload`

- Comprova si una unitat està habilitada:

`systemctl is-enabled {{unitat}}`
