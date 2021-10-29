# head

> Gibt den ersten Teil einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/head>.

- Gebe die ersten 'count_of_lines' Zeilen der Datei 'filename' aus:

`head -n {{count_of_lines}} {{filename}}`

- Gebe die ersten 'size_in_bytes' Bytes der Datei 'filename' aus:

`head -c {{size_in_bytes}} {{filename}}`

- Gebe alle bis auf die letzten 'count_of_lines' Zeilen der Datei 'filename' aus:

`head -n -{{count_of_lines}} {{filename}}`

- Gebe alle bis auf die letzten 'size_in_bytes' Bytes der Datei 'filename' aus:

`head -c -{{size_in_bytes}} {{filename}}`
