# locate

> Zum schnellen finden von Dateinamen.
> Weitere Informationen: <https://manned.org/locate>.

- Sucht nach Dateien in der Datenbanl. Hinweis: Die Datenbank wird periodisch (für gewöhnlich täglich oder wöchentlich) aktualisiert.

`locate {{muster}}`

- Suche nach Dateien mit dem exakten Dateinamen. (Ein Muster ohne Platzhalterzeichen wird als `*muster*` interpretiert):

`locate */{{dateiname}}`

- Neu berechnen der Datenbank. Dies ist nötig, falls kürzlich hinzugefügte Datein gefunden werden sollen:

`sudo updatedb`
