# make

> Taakuitvoerder voor doelen beschreven in Makefile.
> Wordt meestal gebruikt om de compilatie van een uitvoerbaar bestand uit broncode te beheren.
> Meer informatie: <https://www.gnu.org/software/make/manual/make.html>.

- Roep het eerste doel aan dat in de Makefile is gespecificeerd (meestal "all" genoemd):

`make`

- Roep een specifiek doel aan:

`make {{doel}}`

- Roep een specifiek doel aan en voer 4 taken tegelijk uit in parallel:

`make {{[-j|--jobs]}} 4 {{doel}}`

- Gebruik een specifieke Makefile:

`make {{[-f|--file]}} {{pad/naar/bestand}}`

- Voer make uit vanuit een andere map:

`make {{[-C|--directory]}} {{pad/naar/map}}`

- Forceer het maken van een doel, zelfs als bronbestanden ongewijzigd zijn:

`make {{[-B|--always-make]}} {{doel}}`

- Overschrijf een variabele die in de Makefile is gedefinieerd:

`make {{doel}} {{variabele}}={{nieuwe_waarde}}`

- Overschrijf variabelen die in de Makefile zijn gedefinieerd door de omgeving:

`make {{[-e|--environment-overrides]}} {{doel}}`
