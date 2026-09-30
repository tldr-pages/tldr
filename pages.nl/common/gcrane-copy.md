# gcrane copy

> Kopieer efficiënt een image van de ene locatie naar de andere terwijl de digestwaarde behouden blijft.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Kopieer een image van bron naar doel:

`gcrane {{[cp|copy]}} {{bron}} {{doel}}`

- Stel het maximale aantal gelijktijdige kopieën in, standaard is 20:

`gcrane copy {{bron}} {{doel}} {{[-j|--jobs]}} {{aantal_kopieën}}`

- Doorzoek repositories recursief:

`gcrane copy {{bron}} {{doel}} {{[-r|--recursive]}}`

- Toon de help:

`gcrane copy {{[-h|--help]}}`
