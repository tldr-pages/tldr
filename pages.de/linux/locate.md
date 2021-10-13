# locate
> Zum schnellen finden von Dateinamen.
> Weitere Informationen: https://geek-university.com/linux-deutsch/suchen-mit-locate/

- Sucht nach Dateien anhand von Mustern. Das System wird dabei nicht live durchsucht, sondern es wird in einer Datenbnak gesucht. Diese wird periodisch aktualisiert, für gewöhnlich einmal in der Woche oder täglich. Dies bedeutet, dass locate möglichweise Daten nicht findet die seit der letzen aktualisierung der Datenbank hinzugefügt wurden.

`locate {{muster}}`

- Suche nach Dateien mit dem exakten Dateinamen. (Ein Muster ohne Platzhalterzeichen wird als `*muster*` interpretiert):

`locate */{{dateiname}}`

- Neu berechnen der Datenbank. Dies ist nötig, falls kürzlich hinzugefügte Datein gefunden werden sollen:

`sudo updatedb`
