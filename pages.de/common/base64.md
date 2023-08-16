# base64

> Kodieren oder Dekodieren von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/base64>.

- Kodiere den Inhalt einer Datei als base64 und schreibe das Ergebnis nach `stdout`:

`base64 {{datei_name}}`

- Dekodiere den Inhalt einer Datei als base64 und schreibe das Ergebnis nach `stdout`:

`base64 --decode {{datei_name}}`

- Kodiere von `stdin`:

`{{ein_kommando}} | base64`

- Dekodiere von `stdin`:

`{{ein_kommando}} | base64 --decode`
