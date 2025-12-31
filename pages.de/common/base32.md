# base32

> Kodieren oder Dekodieren von Dateien oder Standardeingaben in/aus Base32, zur Standardausgabe.
> Weitere Informationen: <https://manned.org/base32>.

- Kodiere den Inhalt einer Datei als base32 und schreibe das Ergebnis nach `stdout`:

`base32 {{pfad/zu/datei}}`

- Wikkel gecodeerde uitvoer in op een specifieke breedte (`0` schakelt inpakken uit):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{pfad/zu/datei}}`

- Dekodiere den Inhalt einer Datei als base32 und schreibe das Ergebnis nach `stdout`:

`base32 {{[-d|--decode]}} {{pfad/zu/datei}}`

- Kodiere von `stdin`:

`{{befehl}} | base32`

- Dekodiere von `stdin`:

`{{befehl}} | base32 {{[-d|--decode]}}`
