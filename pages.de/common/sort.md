# sort

> Sortiere Zeilen von Textdateien.
> Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Sortiere eine Datei in aufsteigender Reihenfolge:

`sort {{pfad/zu/datei}}`

- Sortiere eine Datei in absteigender Reihenfolge:

`sort {{[-r|--reverse]}} {{pfad/zu/datei}}`

- Sortiere eine Datei ohne Berücksichtigung der Groß-/Kleinschreibung:

`sort {{[-f|--ignore-case]}} {{pfad/zu/datei}}`

- Sortiere eine Datei numerisch statt alphabetisch:

`sort {{[-n|--numeric-sort]}} {{pfad/zu/datei}}`

- Sortiere `/etc/passwd` ab dem dritten Feld jeder Zeile numerisch, verwende `:` als Feldtrennzeichen:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3n /etc/passwd`

- Wie oben, aber wenn die Elemente im dritten Feld gleich sind, sortiere nach dem vierten Feld numerisch mit Exponenten:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3,3n {{[-k|--key]}} 4,4g /etc/passwd`

- Sortiere eine Datei und behalte nur eindeutige Zeilen bei:

`sort {{[-u|--unique]}} {{pfad/zu/datei}}`

- Sortiere eine Datei und gib die Ausgabe in die angegebene Ausgabedatei aus (kann verwendet werden, um eine Datei an Ort und Stelle zu sortieren):

`sort {{[-o|--output]}} {{pfad/zu/ausgabedatei}} {{pfad/zu/eingabedatei}}`
