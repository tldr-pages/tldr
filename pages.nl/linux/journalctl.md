# journalctl

> Bevraag het systemd-journaal.
> Zie ook: `dmesg`.
> Meer informatie: <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html>.

- Toon de laatste `n` regels en volg nieuwe berichten (zoals `tail --follow` voor traditionele syslog):

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow]}}`

- Toon alle berichten met prioriteitsniveau 3 (fouten) sinds de laatste keer opstarten voor de laatste afsluiting:

`journalctl {{[-b|--boot]}} -1 {{[-p|--priority]}} 3`

- Toon alle berichten van een specifieke unit:

`journalctl {{[-u|--unit]}} {{unit}}`

- Toon logs voor een gegeven unit sinds de laatste keer dat deze is gestart:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unit}})`

- Filter berichten binnen een tijdsbereik (ofwel een tijdstempel ofwel plaatshouders zoals "yesterday"):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow|...}} {{[-U|--until]}} "{{YYYY-MM-DD HH:MM:SS}}"`

- Toon alle berichten van een specifiek proces:

`journalctl _PID={{proces_id}}`

- Toon alle berichten van een specifiek uitvoerbaar bestand:

`journalctl {{pad/naar/uitvoerbaar_bestand}}`

- Verwijder journaal-logs die ouder zijn dan 2 dagen:

`journalctl --vacuum-time 2d`
