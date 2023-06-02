# mv

> Verschiebe Dateien oder Verzeichnisse oder benenne diese um.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/mv>.

- Verschiebe eine Datei an einen beliebigen Ort:

`mv {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Verschiebe mehrere Dateien in ein anderes Verzeichnis und behalte deren Namen bei:

`mv {{pfad/zu/datei1 pfad/zu/datei2 ...}} {{pfad/zu/ziel_verzeichnis}}`

- Überschreibe bereits existierende Dateien ohne vorherige Bestätigung:

`mv -f {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Überschreibe bereits existierende Dateien nach Bestätigung (unabhängig von Dateirechten):

`mv -i {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Verhindere das Überschreiben existierender Dateien am Zielort:

`mv -n {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`

- Liste Dateien und deren Details auf während sie verschoben werden:

`mv -v {{pfad/zu/datei}} {{pfad/zu/zieldatei}}`
