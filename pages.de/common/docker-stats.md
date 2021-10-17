# docker stats

> Zeige den Ressourcen-Verbrauch von Containern in Echtzeit.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Zeige sich stetig aktualisierende Statistiken von allen laufenden Containern:

`docker stats`

- Zeige sich stetig aktualisierende Statistiken der durch Leerzeichen getrennten Container:

`docker stats {{container_name}}`

- Ändere das Spaltenformat um die CPU Auslastung von Containern in Prozent anzuzeigen:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Zeige Statistiken für alle Container (laufende und gestoppte):

`docker stats --all`

- Deaktiviere die laufende Aktualisierung und zeige nur die aktuellen Statistiken:

`docker stats --no-stream`
