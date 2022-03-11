# aplay

> Command-line Musik Player für den ALSA Soundkarten-Treiber.
> Weitere Informationen: <https://manned.org/aplay>.

- Spiele eine bestimmte Datei (Abtastrate, Bittiefe, etc. werden automatisch für das Dateiformat erkannt):

`aplay {{pfad/zu/datei}}`

- Spiele die ersten 10 Sekunden einer bestimmten Datei mit 2500 Hz:

`aplay --duration={{10}} --rate={{2500}} {{pfad/zu/datei}}`

- Spiele die rohe Datei mit 22050 Hz, mono, 8-bit, als Mu-Lw `.au` Datei:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{pfad/zu/datei}}`
