# crane copy

> Kopieer efficiënt een remote image van bron naar doel terwijl de digest-waarde behouden blijft.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Kopieer een image van bron naar doel:

`crane {{[cp|copy]}} {{bron}} {{doel}}`

- Kopieer alle tags:

`crane {{[cp|copy]}} {{bron}} {{doel}} {{[-a|--all-tags]}}`

- Stel het maximum aantal gelijktijdige kopieën in, standaard is GOMAXPROCS:

`crane {{[cp|copy]}} {{bron}} {{doel}} {{[-j|--jobs]}} {{int}}`

- Voorkom het overschrijven van bestaande tags in het doel:

`crane {{[cp|copy]}} {{bron}} {{doel}} {{[-n|--no-clobber]}}`

- Toon de help:

`crane {{[cp|copy]}} {{[-h|--help]}}`
