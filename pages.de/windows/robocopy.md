# robocopy

> Robustes Kopieren von Dateien und Ordnern.
> Standardmäßig werden Dateien nur kopiert, wenn die Quell- und Zieldatei ein unterschiedliches Änderungsdatum oder eine unterschiedliche Dateigröße haben.
> Weitere Informationen: <https://learn.microsoft.com/de-de/windows-server/administration/windows-commands/robocopy>.

- Alle `.jpg` und `.bmp` Dateien aus dem einen Verzeichnis in ein anderes Verzeichnis kopieren:

`robocopy {{path/to/source}} {{path/to/destination}} {{*.jpg}} {{*.bmp}}`

- Alle Dateien und Unterverzeichnisse kopieren, einschließlich der leeren Verzeichnisse:

`robocopy {{path/to/source}} {{path/to/destination}} /E`

- Ein Verzeichnis spiegeln/synchronisieren. Dabei wird Alles, was nicht in der Quelle vorhanden ist, gelöscht sowie alle Attribute und Berechtigungen übertragen:

`robocopy {{path/to/source}} {{path/to/destination}} /MIR /COPYALL`

- Alle Dateien und Unterverzeichnisse kopieren, ausgenommen der Quelldateien, die älter sind als die vorhandenen Zieldateien:

`robocopy {{path/to/source}} {{path/to/destination}} /E /XO`

- Gibt alle Dateien aus, die 50 MB und größer sind, anstatt sie zu kopieren:

`robocopy {{path/to/source}} {{path/to/destination}} /MIN:{{52428800}} /L`

- Erlaubt das Fortsetzen des Vorgangs bei Netzwerkverlust, begrenzt die Anzahl an Versuchen auf 5 und die Wartezeit zwischen Versuchen auf 15 Sekunden:

`robocopy {{path/to/source}} {{path/to/destination}} /Z /R:5 /W:15`

- Gibt detaillierte Nutzungshinweise aus:

`robocopy /?`
