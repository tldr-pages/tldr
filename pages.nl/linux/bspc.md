# bspc

> Configureer en bestuur `bspwm`, en beheer nodes, bureaubladen, monitors en meer.
> Zie ook: `bspwm`.
> Meer informatie: <https://github.com/baskerville/bspwm/blob/master/doc/bspwm.1.asciidoc>.

- Definieer twee virtuele bureaubladen:

`bspc monitor {{[-d|--reset-desktops]}} {{bureaublad_naam1}} {{bureaublad_naam2}}`

- Focus op het gegeven bureaublad:

`bspc desktop {{[-f|--focus]}} {{nummer}}`

- Sluit de vensters die afgetakt zijn van de geselecteerde node:

`bspc node {{[-c|--close]}}`

- Stuur de geselecteerde node naar het opgegeven bureaublad:

`bspc node {{[-d|--to-desktop]}} {{nummer}}`

- Schakel de modus volledig scherm in voor de geselecteerde node:

`bspc node {{[-t|--state]}} ~fullscreen`

- Zet de waarde van een specifieke instelling:

`bspc config {{instelling}} {{waarde}}`
