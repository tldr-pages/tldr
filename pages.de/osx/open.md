# open

> Öffnet Dateien, Verzeichnisse und Anwendungen.

- Öffnet eine Datei mit der zugehörigen Anwendung:

`open {{file.ext}}`

- Ausführen einer grafischen macOS-Anwendung:

`open -a {{Application}}`

- Ausführen einer grafischen macOS-Anwendung basierend auf der Bundle-Kennung (siehe `osascript` für eine einfache Möglichkeit, diese zu identifizieren):

`open -b {{com.domain.application}}`

- Öffnen des aktuellen Verzeichnis im Finder:

`open .`

- Zeigen Sie eine Datei im Finder an:

`open -R {{path/to/file}}`

- Alle Dateien einer bestimmten Erweiterung im aktuellen Verzeichnis mit der zugehörigen Anwendung öffnen:

`open {{*.ext}}`
