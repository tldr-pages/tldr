# cat

> Ausgabe und Verkettung von einzelnen Dateien.

- Ausgabe der Inhalte einer Datei an die Standardausgabe:

`cat {{datei}}`

- Verkettung mehrerer einzelner Dateien in eine Zieldatei:

`cat {{datei1}} {{datei2}} > {{ziel_datei}}`

- Anhängen mehrerer Dateien in eine Ziekdatei:

`cat {{datei1}} {{datei2}} >> {{ziel_datei}}`

- Nummerierung aller ausgegebenen Zeilen:

`cat -n {{datei}}`

- Ausgabe inklusive aller unsichtbaren Leerzeichen (mit `M-` Präfix wenn sie nicht ASCII sind):

`cat -v -t -e {{datei}}`
