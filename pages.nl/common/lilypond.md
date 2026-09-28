# lilypond

> Zet muziek en/of produceer MIDI vanuit een bestand.
> Zie ook: `musescore`.
> Meer informatie: <https://lilypond.org/doc/latest/Documentation/usage/command_002dline-usage>.

- Compileer een lilypond-bestand naar een PDF:

`lilypond {{pad/naar/bestand}}`

- Compileer naar het opgegeven formaat:

`lilypond {{[-f|--format]}} {{formaat_dump}} {{pad/naar/bestand}}`

- Compileer het opgegeven bestand, zonder voortgangsupdates te tonen:

`lilypond {{[-s|--silent]}} {{pad/naar/bestand}}`

- Compileer het opgegeven bestand en specificeer ook de bestandsnaam van de uitvoer:

`lilypond {{[-o|--output]}} {{pad/naar/uitvoer_bestand}} {{pad/naar/invoer_bestand}}`

- Toon de versie:

`lilypond {{[-v|--version]}}`
