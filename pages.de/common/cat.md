# cat

> Verkette und gib einzelne oder mehrere Dateien aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cat>.

- Gib den Inhalt einer Datei aus:

`cat {{pfad/zu/datei}}`

- Verkette mehrere Dateien und speichere das Ergebnis in einer neuen Datei:

`cat {{pfad/zu/datei1 pfad/zu/datei2 ...}} > {{pfad/zu/ziel_datei}}`

- Verkette mehrere Dateien und hänge das Ergebnis an eine Datei an:

`cat {{pfad/zu/datei1 pfad/zu/datei2 ...}} >> {{pfad/zu/ziel_datei}}`

- Kopiere den Inhalt einer Datei in eine Ausgabedatei ohne zu puffern:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Schreibe `stdin` in eine Datei:

`cat - > {{pfad/zu/datei}}`
