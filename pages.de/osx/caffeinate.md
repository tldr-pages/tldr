# caffeinate

> Hindert den Mac daran, in den Schlaf-Modus zu gehen.
> Weitere Informationen: <https://ss64.com/osx/caffeinate.html>.

- Halte den Mac für 1 Stunde (3600 Sekunden) wach:

`caffeinate -u -t {{3600}}`

- Halte den Mac wach, bis ein bestimmter Befehl abgeschlossen ist:

`caffeinate -s {{befehl}}`

- Halte den Mac wach, bis `caffeinate` durch Cmd-C beendet wird:

`caffeinate -i`
