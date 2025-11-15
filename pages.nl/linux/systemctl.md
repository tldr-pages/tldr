# systemctl

> Beheer het systemd-systeem en de service manager.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Toon alle actieve services:

`systemctl status`

- Toon gefaalde eenheden:

`systemctl --failed`

- Start/Stop/Herstart/Herlaad/Toon de status van een service:

`systemctl {{start|stop|restart|reload|status}} {{eenheid}}`

- Schakel een eenheid die bij het opstarten wordt uitgevoerd in/uit:

`systemctl {{enable|disable}} {{eenheid}}`

- Herlaad systemd, scan voor nieuwe of veranderde eenheden:

`systemctl daemon-reload`

- Controleer of een eenheid actief/ingeschakeld/gefaald is:

`systemctl {{is-active|is-enabled|is-failed}} {{eenheid}}`

- Toon alle service/socket/automount eenheden, waarbij wordt gefilterd op de actief/gefaald status:

`systemctl list-units {{[-t|--type]}} {{service|socket|automount}} --state {{failed|running}}`

- Toon of bewerk de inhoud en het absolute pad van een eenheidsbestand:

`systemctl {{cat|edit}} {{eenheid}}`
