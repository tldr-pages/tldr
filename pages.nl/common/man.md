# man

> Formatteer en toon handleidingen.
> Meer informatie: <https://www.manned.org/man>.

- Toon de handleiding voor een commando:

`man {{commando}}`

- Toon de handleiding voor een commando uit sectie 7:

`man {{7}} {{commando}}`

- Toon alle beschikbare secties voor een commando:

`man -f {{commando}}`

- Toon het pad dat wordt doorzocht voor handleidingen:

`man --path`

- Toon de locatie van een handleiding in plaats van de handleiding zelf:

`man -w {{commando}}`

- Toon de handleiding in een specifieke taal:

`man {{commando}} --locale={{taal}}`

- Zoek naar handleidingen die een zoekterm bevatten:

`man -k "{{zoekterm}}"`
