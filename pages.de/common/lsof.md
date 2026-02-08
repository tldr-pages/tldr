# lsof

> Liste offene Dateien und die entsprechenden Prozesse auf.
> Hinweis: Root-Rechte sind erforderlich, um Dateien zu listen, die von anderen geöffnet wurden.
> Weitere Informationen: <https://manned.org/lsof>.

- Finde die Prozesse, die eine bestimmte Datei offen haben:

`lsof {{pfad/zu/datei}}`

- Finde den Prozess, der einen lokalen Internet-Port geöffnet hat:

`lsof -i :{{port}}`

- Gib nur die Prozess-ID (PID) aus:

`lsof -t {{pfad/zu/datei}}`

- Liste Dateien auf, die vom angegebenen Benutzer geöffnet wurden:

`lsof -u {{benutzername}}`

- Liste Dateien auf, die vom angegebenen Befehl oder Prozess geöffnet wurden:

`lsof -c {{prozess_oder_befehlsname}}`

- Liste Dateien auf, die von einem bestimmten Prozess geöffnet wurden, angegeben durch seine PID:

`lsof -p {{PID}}`

- Liste offene Dateien in einem Verzeichnis auf:

`lsof +D {{pfad/zu/verzeichnis}}`

- Finde den Prozess, der auf einem lokalen IPv6-TCP-Port lauscht und konvertiere Netzwerk- oder Portnummern nicht:

`lsof -i6TCP:{{port}} -sTCP:LISTEN -n -P`
