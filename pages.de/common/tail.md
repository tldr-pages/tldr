# tail

> Gib das Ende einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Zeige die letzten Zeilen einer Datei an:

`tail {{[-n|--lines]}} {{anzahl_an_zeilen}} {{datei}}`

- Zeige alle Zeilen einer Datei ab einer bestimmten Zeile an:

`tail {{[-n|--lines]}} +{{zeile}} {{datei}}`

- Zeige die letzten Bytes einer Datei an:

`tail {{[-n|--lines]}} {{anzahl_an_bytes}} {{datei}}`

- Lies aus einer Datei, bis `<Ctrl c>` gedrückt wird:

`tail {{[-f|--follow]}} {{datei}}`

- Lies aus einer Datei, bis `<Ctrl c>` gedrückt wird, selbst, wenn die Datei nicht zugänglich ist:

`tail {{[-F|--retry --follow]}} {{datei}}`

- Zeige die letzten Zeilen einer Datei an und lade alle paar Sekunden neu:

`tail {{[-n|--lines]}} {{anzahl_an_zeilen}} {{[-s|--sleep-interval]}} {{anzahl_an_sekunden}} {{[-f|--follow]}} {{datei}}`
