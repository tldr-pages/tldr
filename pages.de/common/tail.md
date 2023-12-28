# tail

> Gib das Ende einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/tail>.

- Zeige die letzten Zeilen einer Datei an:

`tail --lines {{anzahl_an_zeilen}} {{datei}}`

- Zeige alle Zeilen einer Datei ab einer bestimmten Zeile an:

`tail --lines +{{zeile}} {{datei}}`

- Zeige die letzten Bytes einer Datei an:

`tail --bytes {{anzahl_an_bytes}} {{datei}}`

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird:

`tail --follow {{datei}}`

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird, selbst, wenn die Datei nicht zugänglich ist:

`tail --retry --follow {{datei}}`

- Zeige die letzten Zeilen einer Datei an und lade alle paar Sekunden neu:

`tail --lines {{anzahl_an_zeilen}} --sleep-interval {{anzahl_an_sekunden}} --follow {{datei}}`
