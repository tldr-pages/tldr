# mv

> Verschiebe Dateien oder Verzeichnisse oder benenne diese um.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Verschiebe eine Datei an einen beliebigen Ort:

`mv {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Verschiebe mehrere Dateien in ein anderes Verzeichnis und behalte deren Namen bei:

`mv {{pfad/zu/datei1 pfad/zu/datei2 ...}} {{pfad/zu/ziel_verzeichnis}}`

- Überschreibe bereits existierende Dateien ohne vorherige Bestätigung:

`mv {{[-f|--force]}} {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Überschreibe bereits existierende Dateien nach Bestätigung (unabhängig von Dateirechten):

`mv {{[-i|--interactive]}} {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Verhindere das Überschreiben existierender Dateien am Zielort:

`mv {{[-n|--no-clobber]}} {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Liste Dateien und deren Details auf während sie verschoben werden:

`mv {{[-v|--verbose]}} {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`
