# docker system

> Verwalte Docker Daten und zeige systemweite Informationen an.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/system/>.

- Zeige Hilfe:

`docker system`

- Zeige Docker Festplattennutzung:

`docker system df`

- Zeige detaillierte Informationen zur Festplattennutzung:

`docker system df --verbose`

- Entferne nicht-verwendete Daten:

`docker system prune`

- Entferne nicht-verwendete Daten, die älter als die angegebene Zeit sind:

`docker system prune --filter="until={{stunden}}h{{minuten}}m"`

- Zeige Echtzeit-Events vom Docker Daemon:

`docker system events`

- Zeige Echtzeit-Events von Containern und formatiere jede Zeile als gültiges JSON:

`docker system events --filter 'type=container' --format '{{json .}}'`

- Zeige systemweite Informationen:

`docker system info`
