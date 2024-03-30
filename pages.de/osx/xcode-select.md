# xcode-select

> Wechsel zwischen verschiedenen Xcode Versionen und den enthaltenen Entwicklertools.
> Wird auch verwendet, um den Pfad zu Xcode zu aktualisieren, wenn dieser sich nach einer Installation geändert hat.
> Weitere Informationen: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Installiere die Xcode Entwicklertools:

`xcode-select --install`

- Wähle einen bestimmten Pfad als aktives Entwicklerverzeichnis aus:

`xcode-select --switch {{pfad/zu/Xcode.app/Contents/Developer}}`

- Wähle eine Xcode Version aus und ändere das aktive Entwicklerverzeichnis dahin:

`xcode-select --switch {{pfad/zu/Xcode.app}}`

- Gib das derzeit aktive Entwicklerverzeichnis aus:

`xcode-select --print-path`

- Verwerfe alle vom Benutzer angegebenen Entwicklerverzeichnisse (fortan wird der Standardsuchmechanismus verwendet, um diese zu finden):

`sudo xcode-select --reset`
