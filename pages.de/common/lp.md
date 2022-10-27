# lp

> Druckt Dateien.
> Weitere Informationen: <https://manned.org/lp>.

- Drucke die Ausgabe eines Befehls mit dem Standard-Drucker (siehe `lpstat`):

`echo "test" | lp`

- Drucke eine Datei mit dem Standard-Drucker:

`lp {{pfad/zu/datei}}`

- Drucke eine Datei mit einem bestimmten Drucker (siehe `lpstat`):

`lp -d {{druckername}} {{pfad/zu/datei}}`

- Drucke N Kopien einer Datei mit dem Standarddrucker (wobei N die Anzahl gewünschter Kopien ist):

`lp -n {{N}} {{pfad/zu/datei}}`

- Drucke nur bestimmte Seiten mit dem Standarddrucker (drucke Seiten 1, 3-5 und 16):

`lp -P 1,3-5,16 {{pfad/zu/datei}}`

- Führe einen aufgehaltenen Druckauftrag durch:

`lp -i {{job_id}} -H resume`
