# musescore

> MuseScore bladmuziek bewerker.
> Zie ook: `lilypond`.
> Meer informatie: <https://handbook.musescore.org/appendix/command-line-usage>.

- Stel de MP3 uitvoer bitsnelheid in kbit/s:

`musescore {{[-b|--bitrate]}} {{bitsnelheid}}`

- Open MuseScore in debug modus:

`musescore {{[-d|--debug]}}`

- Schakel experimentele funcies in, bijvoorbeeld lagen:

`musescore {{[-e|--experimental]}}`

- Exporteer het gegeven bestand naar het gegeven uitvoer bestand. Het bestandstype hangt af van de gegeven extentie:

`musescore {{[-o|--export-to]}} {{uitvoer_bestand}} {{invoer_bestand}}`

- Geef het verschil tussen de gegeven partituren:

`musescore --diff {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Specificeer een MIDI invoer operaties bestand:

`musescore {{[-M|--midi-operations]}} {{pad/naar/bestand}}`
