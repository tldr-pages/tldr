# alias

> Maak een alias aan -- Woorden die vervangen worden door commando's.
> Een alias blijft bestaan in de huidige shell sessie, tenzij gedefinieerd in de configuratie van de shell, bijvoorbeeld in `~/.bashrc`.
> Zie ook: `unalias`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>.

- Toon alle aliassen:

`alias`

- Maak een generieke alias aan:

`alias {{woord}}="{{commando}}"`

- Laat het gekoppelde commando zien van een gegeven alias:

`alias {{woord}}`

- Verwijder een alias:

`unalias {{woord}}`

- Maak van `rm` een interactief commando:

`alias {{rm}}="{{rm -i}}"`

- Maak een alias `la` aan als korte schrijfwijze van `ls -a`:

`alias {{la}}="{{ls -a}}"`
