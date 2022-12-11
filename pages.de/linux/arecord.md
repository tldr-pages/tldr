# arecord

> Sound Recorder für den ALSA-Soundkarten-Treiber.
> Weitere Informationen: <https://manned.org/arecord>.

- Nehme einen Schnipsel in CD-Qualität auf (beende die Aufnahme mit CTRL-C):

`arecord -vv --format=cd {{pfad/zur/datei.wav}}`

- Nehme einen Schnipsel in CD-Qualität auf mit einer festen Länge von 10 Sekunden:

`arecord -vv --format=cd --duration={{10}} {{pfad/zur/datei.wav}}`

- Nehme einen Schnipsel auf und speichere es als MP3 (beende die Aufnahme mit CTRL-C):

`arecord -vv --format=cd --file-type raw | lame -r - {{path/to/file.mp3}}`

- Liste alle Soundkarten und digitalen Ausgabe Geräte:

`arecord --list-devices`

- Benutze das interaktive Interface (z.B. Space oder Enter für Play oder Pause):

`arecord --interactive`
