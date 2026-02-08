# join

- Verbinde zwei Dateien auf dem ersten (Standard) Feld:

`join {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Verbinde zwei Dateien mit einem Komma (statt einem Leerzeichen) als Feldtrennzeichen:

`join -t ',' {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Verbinde Feld 3 von Datei1 mit Feld 1 von Datei2:

`join -1 {{3}} -2 {{1}} {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Erzeuge eine Zeile für jede nicht zuordenbare Zeile für Datei1:

`join -a {{1}} {{pfad/zu/datei1}} {{pfad/zu/datei2}}`

- Verbinde eine Datei aus `stdin`:

`cat {{pfad/zu/datei1}} | join - {{pfad/zu/datei2}}`
