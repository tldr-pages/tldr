# musescore

> MuseScore 3 bladmuziek bewerker.
> Meer informatie: <https://musescore.org/en/handbook/3/command-line-options>.

- Gebruik een specifiek audio stuurprogramma:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- Stel de MP3 uitvoer bitsnelheid in kbit/s:

`musescore --bitrate {{bitsnelheid}}`

- Open MuseScore in debug modus:

`musescore --debug`

- Schakel experimentele funcies in, bijvoorbeeld lagen:

`musescore --experimental`

- Exporteer het gegeven bestand naar het gegeven uitvoer bestand. Het bestandstype hangt af van de gegeven extentie:

`musescore --export-to {{uitvoer_bestand}} {{invoer_bestand}}`

- Geef het verschil tussen de gegeven partituren:

`musescore --diff {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Specificeer een MIDI invoer operaties bestand:

`musescore --midi-operations {{pad/naar/bestand}}`
