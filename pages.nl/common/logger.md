# logger

> Voeg berichten toe aan syslog (/var/log/syslog).
> Meer informatie: <https://manned.org/logger>.

- Log een bericht naar syslog:

`logger {{bericht}}`

- Neem invoer van `stdin` en log naar syslog:

`echo {{log_entry}} | logger`

- Stuur de uitvoer naar een externe syslog-server die op een bepaalde poort draait. Standaardpoort is 514:

`echo {{log_entry}} | logger --server {{hostname}} --port {{poort}}`

- Gebruik een specifieke tag voor elke gelogde regel. Standaard is de naam van de ingelogde gebruiker:

`echo {{log_entry}} | logger --tag {{tag}}`

- Log berichten met een gegeven prioriteit. Standaard is `user.notice`. Zie `man logger` voor alle prioriteitsopties:

`echo {{log_entry}} | logger --priority {{user.warning}}`
