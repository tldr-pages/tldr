# nodemon

> Beobachtet Dateien und startet Node Applikationen automatisch neu, wenn Änderungen erkannt wurden.
> Weitere Informationen: <https://nodemon.io>.

- Führe die angegebene Datei aus und warte auf Änderungen:

`nodemon {{path/to/file.js}}`

- Manueller Neustart von Nodemon (beachte, dass Nodemon dabei aktiv sein muss):

`rs`

- Ignoriere bestimmte Dateien:

`nodemon --ignore {{path/to/file_or_directory}}`

- Übergib Argumente an die Node Applikation:

`nodemon {{path/to/file.js}} {{arguments}}`

- Führe Nicht-Node Skripte aus:

`nodemon --exec "{{python --verbose}}" {{path/to/file.py}}`
