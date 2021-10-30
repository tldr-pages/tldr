# cat

> Verkette und gib einzelne oder mehrere Dateien aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cat>.

- Gib den Inhalt einer Datei aus:

`cat {{pfad/zu/datei}}`

- Verkette mehrere Dateien und speichere das Ergebnis in einer neuen Datei:

`cat {{pfad/zu/datei1}} {{pfad/zu/datei2}} > {{pfad/zu/ziel_datei}}`

- Verkette mehrere Dateien und hänge das Ergebnis an eine Datei an:

`cat {{pfad/zu/datei1}} {{pfad/zu/datei2}} >> {{pfad/zu/ziel_datei}}`

- Nummeriere alle ausgegebenen Zeilen:

`cat -n {{pfad/zu/datei}}`

- Gib eine Datei inklusive aller unsichtbaren Leerzeichen aus (mit `M-` Präfix wenn sie nicht ASCII sind):

`cat -v -t -e {{pfad/zu/datei}}`
