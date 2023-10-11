# del

> Lösche eine oder mehrere Dateien.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Lösche eine oder mehrere durch Leerzeichen getrennte Dateien oder Dateimuster:

`del {{dateimuster}}`

- Fordere vor dem Löschen jeder Datei zur Bestätigung auf:

`del {{dateimuster}} /p`

- Erzwinge das Löschen von schreibgeschützten Dateien:

`del {{dateimuster}} /f`

- Lösche alle Dateien die dem Muster entsprechen rekursiv in allen Unterordnern:

`del {{dateimuster}} /s`

- Zeige keine Eingabeaufforderung wenn Dateien basierend auf einem globalen Platzhalter gelöscht werden sollen:

`del {{dateimuster}} /q`

- Zeige Hilfe an und liste verfügbare Attribute auf:

`del /?`

- Lösche Dateien mit den gegebenen Attributen:

`del {{dateimuster}} /a {{attribut}}`
