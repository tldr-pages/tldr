# cat

> Verkette und gib einzelne oder mehrere Dateien aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/cat>.

- Gib den Inhalt einer Datei aus:

`cat {{pfad/zu/datei}}`

- Verkette mehrere Dateien und speichere das Ergebnis in einer neuen Datei:

`cat {{pfad/zu/datei1 pfad/zu/datei2 ...}} > {{pfad/zu/ziel_datei}}`

- Verkette mehrere Dateien und hänge das Ergebnis an eine Datei an:

`cat {{pfad/zu/datei1 pfad/zu/datei2 ...}} >> {{pfad/zu/ziel_datei}}`

- Kopieren den Inhalt einer Datei ohne Pufferung in eine Ausgabedatei:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Schreib `stdin` in eine Datei:

`cat - > {{pfad/zu/datei}}`
