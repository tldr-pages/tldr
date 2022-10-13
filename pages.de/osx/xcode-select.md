# xcode-select

> Wechsel zwischen verschiedenen Xcode Versionen und den enthaltenen Entwicklertools.
> Wird auch verwendet, um den Pfad zu Xcode zu aktualisieren, wenn dieser sich nach einer Installation geändert hat.
> Mehr Informationen: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Installieren der Xcode Entwicklertools:

`xcode-select --install`

- Auswählen eines bestimmten Pfads als aktives Entwicklerverzeichnis:

`sudo xcode-select --switch {{pfad/zu/Xcode.app/Contents/Developer}}`

- Auswählen der gegebenen Xcode-Instanz (falls mehrere Versionen installiert sind) und ändert das aktive Entwicklerverzeichnis:

`sudo xcode-select --switch {{pfad/zu/Xcode.app}}`

- Gebe das derzeit aktive Entwicklerverzeichnis auf der Konsole aus:

`xcode-select --print-path`

- Verwerfe alle vom Benutzer angegebenen Entwicklerverzeichnisse. Der Standardsuchmechanismus wird dann verwendet, um diese zu finden:

`sudo xcode-select --reset`
