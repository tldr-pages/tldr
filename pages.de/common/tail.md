# tail

> Gibt das Ende einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/tail>.

- Zeige die letzten 'num' Zeilen der Datei 'file' an:

`tail -n {{num}} {{file}}`

- Zeige alle Zeilen der Datei 'file' ab Zeile 'num' an:

`tail -n +{{num}} {{file}}`

- Zeige die letzten 'num' Bytes der Datei 'file' an:

`tail -c {{num}} {{file}}`

- Lese aus der Datei 'file', bis `Ctrl + C` gedrückt wird:

`tail -f {{file}}`

- Lese aus der Datei 'file', bis `Ctrl + C` gedrückt wird, selbst, wenn 'file' nicht zugänglich ist:

`tail -F {{file}}`

- Zeige die letzten 'num' Zeilen der Datei 'file' an und lade alle 'n' Sekunden neu:

`tail -n {{num}} -s {{n}} -f {{file}}`
