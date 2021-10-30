# tail

> Gibt das Ende einer Datei aus.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/tail>.

- Zeige die letzten 'anzahl' Zeilen der Datei 'datei' an:

`tail -n {{anzahl}} {{datei}}`

- Zeige alle Zeilen der Datei 'datei' ab Zeile 'anzahl' an:

`tail -n +{{anzahl}} {{datei}}`

- Zeige die letzten 'anzahl' Bytes der Datei 'datei' an:

`tail -c {{anzahl}} {{datei}}`

- Lese aus der Datei 'datei', bis `Ctrl + C` gedrückt wird:

`tail -f {{datei}}`

- Lese aus der Datei 'datei', bis `Ctrl + C` gedrückt wird, selbst, wenn 'datei' nicht zugänglich ist:

`tail -F {{datei}}`

- Zeige die letzten 'anzahl' Zeilen der Datei 'datei' an und lade alle 'n' Sekunden neu:

`tail -n {{anzahl}} -s {{n}} -f {{datei}}`
