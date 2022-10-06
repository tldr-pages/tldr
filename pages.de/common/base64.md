# base64

> Kodierung oder Dekodierung von Dateien oder Standardeingaben in und aus Base64, zur Standardausgabe (stdout).
> Weitere Informationen: <https://www.gnu.org/software/coreutils/base64>.

- Kodiert den Inhalt einer Datei als base64 und schreibt das Ergebnis nach stdout:

`base64 {{filename}}`

- Dekodiert den Inhalt einer Datei als base64 und schreibt das Ergebnis nach stdout:

`base64 --decode {{filename}}`

- Kodiert von stdin:

`{{somecommand}} | base64`

- Dekodiert von stdin:

`{{somecommand}} | base64 --decode`
