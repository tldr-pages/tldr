# crane copy

> Kopieer efficiënt een remote image van bron naar doel terwijl de digest-waarde behouden blijft.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Kopieer een image van bron naar doel:

`crane copy {{bron}} {{doel}}`

- Kopieer alle tags:

`crane copy {{bron}} {{doel}} {{[-a|--all-tags]}}`

- Stel het maximum aantal gelijktijdige kopieën in, standaard is GOMAXPROCS:

`crane copy {{bron}} {{doel}} {{[-j|--jobs]}} {{int}}`

- Voorkom het overschrijven van bestaande tags in het doel:

`crane copy {{bron}} {{doel}} {{[-n|--no-clobber]}}`

- Toon de help:

`crane copy {{[-h|--help]}}`
