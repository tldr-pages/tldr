# gcrane copy

> Kopieer efficiënt een afbeelding van de ene locatie naar de andere terwijl de digestwaarde behouden blijft.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Kopieer een afbeelding van bron naar doel:

`gcrane {{[cp|copy]}} {{bron}} {{doel}}`

- Stel het maximale aantal gelijktijdige kopieën in, standaard is 20:

`gcrane copy {{bron}} {{doel}} {{[-j|--jobs]}} {{aantal_kopieën}}`

- Of de repositories doorzocht moeten worden:

`gcrane copy {{bron}} {{doel}} {{[-r|--recursive]}}`

- Toon de help:

`gcrane copy {{[-h|--help]}}`
