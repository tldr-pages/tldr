# tee

> Lies aus `stdin` und schreibe nach `stdout` und Dateien (oder Befehle).
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- Kopiere `stdin` in jede Datei und auch nach `stdout`:

`echo "example" | tee {{pfad/zu/datei}}`

- Hänge an die angegebenen Dateien an, überschreibe sie nicht:

`echo "example" | tee {{[-a|--append]}} {{pfad/zu/datei}}`

- Gib `stdin` auf dem Terminal aus und pipe es auch in ein anderes Programm zur Weiterverarbeitung:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Erstelle ein Verzeichnis namens "example", zähle die Anzahl der Zeichen in "example" und gib "example" auf dem Terminal aus:

`echo "example" | tee >(xargs mkdir) >(wc {{[-c|--bytes]}})`