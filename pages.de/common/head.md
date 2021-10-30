# head

> Gibt den ersten Teil einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/head>.

- Gebe die ersten Zeilen einer Datei aus:

`head -n {{anzahl_zeilen}} {{datei}}`

- Gebe die ersten Bytes einer Datei aus:

`head -c {{anzahl_bytes}} {{datei}}`

- Gebe alle bis auf die letzten Zeilen einer Datei aus:

`head -n -{{anzahl_zeilen}} {{datei}}`

- Gebe alle bis auf die letzten Bytes einer Datei aus:

`head -c -{{anzahl_bytes}} {{datei}}`
