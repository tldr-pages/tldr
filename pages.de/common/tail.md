# tail

> Gib das Ende einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/tail>.

- Zeige die letzten Zeilen einer Datei an:

`tail -n {{anzahl_an_zeilen}} {{datei}}`

- Zeige alle Zeilen einer Datei ab einer bestimmten Zeile an:

`tail -n +{{zeile}} {{datei}}`

- Zeige die letzten Bytes einer Datei an:

`tail -c {{anzahl_an_bytes}} {{datei}}`

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird:

`tail -f {{datei}}`

- Lies aus einer Datei, bis `Ctrl + C` gedrückt wird, selbst, wenn die Datei nicht zugänglich ist:

`tail -F {{datei}}`

- Zeige die letzten Zeilen einer Datei an und lade alle paar Sekunden neu:

`tail -n {{anzahl_an_zeilen}} -s {{anzahl_an_sekunden}} -f {{datei}}`
