# paste

- Verbinde alle Zeilen zu einer einzelnen Zeile, verwende `TAB` als Trennzeichen:

`paste {{[-s|--serial]}} {{pfad/zu/datei}}`

- Verbinde alle Zeilen zu einer einzelnen Zeile, verwende das angegebene Trennzeichen:

`paste {{[-s|--serial]}} {{[-d|--delimiters]}} {{trennzeichen}} {{pfad/zu/datei}}`

- Füge zwei Dateien nebeneinander zusammen, jede in ihrer Spalte, verwende `TAB` als Trennzeichen:

`paste {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Füge zwei Dateien nebeneinander zusammen, jede in ihrer Spalte, verwende das angegebene Trennzeichen:

`paste {{[-d|--delimiters]}} {{trennzeichen}} {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Füge zwei Dateien zusammen, wobei Zeilen abwechselnd hinzugefügt werden:

`paste {{[-d|--delimiters]}} '\n' {{pfad/zu/datei1}} {{pfad/zu/datei2}}`
