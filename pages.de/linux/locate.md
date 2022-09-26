# locate

> Zum schnellen Finden von Dateinamen.
> Weitere Informationen: <https://manned.org/locate>.

- Suche nach Dateien in der Datenbank. Hinweis: Die Datenbank wird periodisch aktualisiert (für gewöhnlich täglich oder wöchentlich):

`locate {{muster}}`

- Suche nach Dateien mit dem exakten Dateinamen. (Ein Muster ohne Platzhalterzeichen wird als `*muster*` interpretiert):

`locate */{{dateiname}}`

- Aktualisiere die Datenbank. Dies ist nötig, falls kürzlich hinzugefügte Dateien gefunden werden sollen:

`sudo updatedb`
