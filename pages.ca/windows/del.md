# del

> Lösche eine oder mehrere Dateien.
> Mehr Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Lösche eine oder mehrere durch Leerzeichen getrennte Dateien oder Datei-Muster (Datei-Namen mit Platzhaltern, "Wildcards"):

`del {{datei_muster}}`

- Fordere vor dem Löschen jeder Datei zur Bestätigung auf:

`del {{datei_muster}} /p`

- Erzwinge das Löschen von schreibgeschützten Dateien:

`del {{datei_muster}} /f`

- Lösche rekursiv alle Dateien die dem Muster entsprechen in allen Unterordnern:

`del {{datei_muster}} /s`

- Keine Eingabeaufforderung wenn Dateien basierend auf einem globalen Platzhalter gelöscht werden sollen:

`del {{datei_muster}} /q`

- Hilfe anzeigen und verfügbare Attribute auflisten:

`del /?`

- Lösche Dateien mit gegebenen Attributen:

`del {{datei_muster}} /a {{attribut}}`
