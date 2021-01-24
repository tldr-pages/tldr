# caffeinate

> Hindert den Mac daran in den Schlaf-Modus zu gehen.

- Verhindern, dass der Mac für 1 Stunde (3600 Sekunden) schläft:

`caffeinate -u -t {{3600}}`

- Verhindern, dass der Mac schläft, bis der Befehl abgeschlossen ist:

`caffeinate -s {{command}}`

- Verhindern, dass der Mac in den Schlaf-Modus geht, bis Sie Control-C eingeben:

`caffeinate -i`
