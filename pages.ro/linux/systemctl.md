# systemctl

> Controlați sistemul systemd și managerul de servicii.
> Mai multe informaţii: <https://www.freedesktop.org/software/systemd/man/systemctl.html>

- Lista unităților eșuate:

`systemctl --failed`

- Start/Stop/repornește/Reîncărcați un serviciu:

`systemctl {{start|stop|restart|reload}} {{unit}}`

- Afișați starea unei unități:

`systemctl status {{unit}}`

- Activează/dezactivează o unitate care urmează să fie pornită la bootup:

`systemctl {{enable|disable}} {{unit}}`

- Masca/Demascați o unitate pentru a preveni activarea și activarea manuală:

`systemctl {{mask|unmask}} {{unit}}`

- Reîncărcați systemd, scanați pentru unități noi sau modificate:

`systemctl daemon-reload`

- Verificați dacă o unitate este activă:

`systemctl is-active {{unit}}`

- Verificați dacă o unitate este activată:

`systemctl is-enabled {{unit}}`
