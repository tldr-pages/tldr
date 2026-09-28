# clementine

> Een moderne muziekspeler en bibliotheekbeheerder.
> Zie ook: `audacious`, `qmmp`, `cmus`, `mpv`.
> Meer informatie: <https://manned.org/clementine>.

- Start de GUI of breng deze naar voren:

`clementine`

- Start het afspelen van muziek:

`clementine {{url|pad/naar/muziek.ext}}`

- Schakel tussen pauzeren en afspelen:

`clementine {{[-t|--play-pause]}}`

- Stop de weergave:

`clementine {{[-s|--stop]}}`

- Ga naar het volgende of vorige nummer:

`clementine --{{next|previous}}`

- Maak een nieuwe afspeellijst met één of meer muziekbestanden of URL's:

`clementine {{[-c|--create]}} {{url1|pad/naar/muziek1.ext url2|pad/naar/muziek2.ext ...}}`

- Laad een afspeellijstbestand:

`clementine {{[-l|--load]}} {{pad/naar/afspeellijst.ext}}`

- Speel een specifiek nummer af in de momenteel geladen afspeellijst:

`clementine {{[-k|--play-track]}} {{5}}`
