# open

> Öffne Dateien, Verzeichnisse und Anwendungen.
> Weitere Informationen: <https://ss64.com/osx/open.html>.

- Öffne eine Datei in der zugehörigen Anwendung:

`open {{pfad/zu/datei}}`

- Führe eine grafische macOS-Anwendung aus:

`open -a {{anwendung}}`

- Führe eine grafische macOS-Anwendung basierend auf der Bundle-Kennung aus (siehe `osascript` für eine einfache Möglichkeit, diese zu identifizieren):

`open -b {{com.domain.anwendung}}`

- Öffne das aktuelle Verzeichnis im Finder:

`open .`

- Zeige eine Datei im Finder an:

`open -R {{pfad/zu/datei}}`

- Öffne alle Dateien einer bestimmten Erweiterung im aktuellen Verzeichnis mit der zugehörigen Anwendung:

`open {{*.ext}}`
