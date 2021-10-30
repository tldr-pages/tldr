# head

> Gibt den ersten Teil einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/head>.

- Gebe die ersten 'anzahl' Zeilen der Datei 'datei' aus:

`head -n {{anzahl}} {{datei}}`

- Gebe die ersten 'anzahl' Bytes der Datei 'datei' aus:

`head -c {{anzahl}} {{datei}}`

- Gebe alle bis auf die letzten 'anzahl' Zeilen der Datei 'datei' aus:

`head -n -{{anzahl}} {{datei}}`

- Gebe alle bis auf die letzten 'anzahl' Bytes der Datei 'datei' aus:

`head -c -{{anzahl}} {{datei}}`
