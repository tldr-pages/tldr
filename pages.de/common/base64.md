# base64

> Kodierung oder Dekodierung von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/base64>.

- Kodiert den Inhalt einer Datei als base64 und schreibt das Ergebnis nach stdout:

`base64 {{datei_name}}`

- Dekodiert den Inhalt einer Datei als base64 und schreibt das Ergebnis nach stdout:

`base64 --decode {{datei_name}}`

- Kodieren von stdin:

`{{ein_kommando}} | base64`

- Dekodieren von stdin:

`{{ein_kommando}} | base64 --decode`
