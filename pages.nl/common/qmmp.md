# qmmp

> Een audiospeler met een interface vergelijkbaar met Winamp of XMMS.
> Zie ook: `clementine`, `ncmpcpp`, `cmus`.
> Meer informatie: <https://manned.org/qmmp>.

- Start de GUI:

`qmmp`

- Start of stop de momenteel afspelende audio:

`qmmp {{[-t|--play-pause]}}`

- Spring een specifieke hoeveelheid tijd in seconden voorwaarts of achterwaarts:

`qmmp --seek-{{fwd|bwd}} {{time_in_seconds}}`

- Speel het volgende audiobestand af:

`qmmp --next`

- Speel het vorige audiobestand af:

`qmmp --previous`

- Toon het huidige volume:

`qmmp --volume-status`

- Verhoog of verlaag het volume van de momenteel afspelende audio met 5%:

`qmmp --volume-{{inc|dec}}`
