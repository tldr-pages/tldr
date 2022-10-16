# del

> Lösche eine oder mehrere Dateien.
> Mehr Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Lösche eine oder mehrere durch Leerzeichen getrennte Dateien oder Datei-Muster (Datei-Namen mit Platzhaltern, "Wildcards"):

`del {{datei_muster}}`

- Fordere vor dem Löschen jeder Datei zur Bestätigung auf:

`del {{datei_muster}} /p`

- Erzwinge das Löschen von schreibgeschützten Dateien:

`del {{datei_muster}} /f`

- Lösche alle Dateien die dem Muster entsprechen rekursiv in allen Unterordnern:

`del {{datei_muster}} /s`

- Zeige keine Eingabeaufforderung wenn Dateien basierend auf einem globalen Platzhalter gelöscht werden sollen:

`del {{datei_muster}} /q`

- Zeige Hilfe an und liste verfügbare Attribute auf:

`del /?`

- Lösche Dateien mit den gegebenen Attributen:

`del {{datei_muster}} /a {{attribut}}`
