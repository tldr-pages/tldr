# mv

> Verschieben oder Umbenennen von Dateien oder Ordnern.

- Verschieben von Dateien an einen beliebigen Ort:

`mv {{quelle}} {{ziel}}`

- Überschreibe bereits existierende Dateien ohne vorherige Bestätigung:

`mv -f {{quelle}} {{ziel}}`

- Überschreibe bereits existierende Dateien nach Bestätigung (unabhängig von Dateirechten):

`mv -i {{quelle}} {{ziel}}`

- Verhindert das Überschreiben existierender Dateien am Zielort:

`mv -n {{quelle}} {{ziel}}`

- Verschieben von Dateien im ausführlichen Modus - inklusive Auflistung während des Kopierens:

`mv -v {{quelle}} {{ziel}}`
