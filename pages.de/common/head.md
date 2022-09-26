# head

> Gibt den ersten Teil einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/head>.

- Gib die ersten paar Zeilen einer Datei aus:

`head -n {{anzahl_an_zeilen}} {{datei}}`

- Gib die ersten Bytes einer Datei aus:

`head -c {{anzahl_an_bytes}} {{datei}}`

- Gib alle bis auf die letzten Zeilen einer Datei aus:

`head -n -{{anzahl_an_zeilen}} {{datei}}`

- Gib alle bis auf die letzten Bytes einer Datei aus:

`head -c -{{anzahl_an_bytes}} {{datei}}`
