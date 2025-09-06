# nodemon

> Beobachtet Dateien und startet Node Applikationen automatisch neu, wenn Änderungen erkannt wurden.
> Weitere Informationen: <https://nodemon.io>.

- Führe die angegebene Datei aus und warte auf Änderungen:

`nodemon {{pfad/zu/datei.js}}`

- Manueller Neustart von Nodemon (beachte, dass Nodemon dabei aktiv sein muss):

`rs`

- Ignoriere bestimmte Dateien:

`nodemon --ignore {{pfad/zu/datei_oder_verzeichnis}}`

- Übergib Argumente an die Node Applikation:

`nodemon {{pfad/zu/datei.js}} {{argumente}}`

- Übergib Argumente an node selbst, wenn sie nicht bereits Argumente von nodemon sind (z.B. `--inspect`):

`nodemon {{argumente}} {{pfad/zu/datei.js}}`

- Führe Nicht-Node Skripte aus:

`nodemon --exec "{{befehl_um_skript_auszuführen}} {{argumente}}" {{pfad/zu/skript}}`

- Führe ein Python-Skript aus:

`nodemon --exec "python {{argumente}}" {{pfad/zu/datei.py}}`
