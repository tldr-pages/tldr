# cat

> Gibt den Inhalt einer Datei in STDOUT aus.
> Mehr Informationen: <https://www.gnu.org/software/coreutils/cat>

- Gebe den Inhalt einer Datei im aktuellen Verzeichnis aus:

`cat {{datei.ext}}`

- Gebe den Inhalt einer Datei in einem anderen Verzeichnis aus:

`cat {{pfad/zur/datei.ext}}`

- Gebe den Inhalt einer Datei aus und nummeriere die Zeilen:

`cat -n {{file.ext}}`

Gebe den Inhalt einer Datei aus und nummeriere alle Zeilen die nicht leer sind:

`cat -b {{file.ext}}
