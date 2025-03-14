# base64

> Kodieren oder Dekodieren von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe.
> Weitere Informationen: <https://manned.org/base64>.

- Kodiere den Inhalt einer Datei als base64 und schreibe das Ergebnis nach `stdout`:

`base64 {{pfad/zu/datei}}`

- Wikkel gecodeerde uitvoer in op een specifieke breedte (`0` schakelt inpakken uit):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{pfad/zu/datei}}`

- Dekodiere den Inhalt einer Datei als base64 und schreibe das Ergebnis nach `stdout`:

`base64 {{[-d|--decode]}} {{pfad/zu/datei}}`

- Kodiere von `stdin`:

`{{befehl}} | base64`

- Dekodiere von `stdin`:

`{{befehl}} | base64 {{[-d|--decode]}}`
