# pio pkg

> Beheer pakketten in het register.
> Pakketten kunnen alleen verwijderd worden binnen 72 uur (3 dagen) vanaf de datum dat ze gepubliceerd zijn.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- Maak een pakket tarball van de huidige map:

`pio pkg pack {{[-o|--output]}} {{pad/naar/pakket.tar.gz}}`

- Maak en publiceer een pakket tarball van de huidige map:

`pio pkg publish`

- Publiceer de huidige map en beperk de publieke toegang:

`pio pkg publish --private`

- Publiceer een pakket:

`pio pkg publish {{pad/naar/pakket.tar.gz}}`

- Publiceer een pakket met een aangepaste release datum (UTC):

`pio pkg publish {{pad/naar/pakket.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- Verwijder alle versies van een gepubliceerd pakket van het register:

`pio pkg unpublish {{pakket}}`

- Verwijder een specifieke versie van een gepubliceerd pakket van het register:

`pio pkg unpublish {{pakket}}@{{version}}`

- Maak de verwijdering ongedaan en zet alle versies of een specifieke versie van het pakket terug in het register:

`pio pkg unpublish --undo {{pakket}}@{{version}}`
