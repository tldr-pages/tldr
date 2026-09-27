# musescore

> MuseScore bladmuziekbewerker.
> Zie ook: `lilypond`.
> Meer informatie: <https://handbook.musescore.org/appendix/command-line-usage>.

- Stel de MP3 uitvoer bitsnelheid in kbit/s:

`musescore {{[-b|--bitrate]}} {{bitsnelheid}}`

- Open MuseScore in debug modus:

`musescore {{[-d|--debug]}}`

- Schakel experimentele functies in, bijvoorbeeld lagen:

`musescore {{[-e|--experimental]}}`

- Exporteer het gegeven bestand naar het gegeven uitvoerbestand. Het bestandstype hangt af van de gegeven extensie:

`musescore {{[-o|--export-to]}} {{uitvoer_bestand}} {{invoer_bestand}}`

- Geef het verschil tussen de gegeven partituren:

`musescore --diff {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Specificeer een MIDI import operaties bestand:

`musescore {{[-M|--midi-operations]}} {{pad/naar/bestand}}`
