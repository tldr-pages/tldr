# aplay

> Commandline Musik Player für den ALSA Soundkarten Treiber.
> Mehr Informationen: <https://manned.org/aplay>.

- Spiele eine spezifische Datei (Sampling Rate, Bit Tiefe, etc. werden automatisch erkannt für das Dateiformat):

`aplay {{pfad/zur/datei}}`

- Spiele die ersten 10 Sekunden einer spezifischen Datei mit 2500Hz:

`aplay --duration={{10}} --rate={{2500}} {{pfad/zur/datei}}`

- Spiele die rohe Datei mit 22050 Hz, mono, 8-bit, als Mu-Lw `.au` Datei:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{pfad/zur/datei}}`
