# bspc

> Een tool om `bspwm` te besturen.
> Bekijk ook: `bspwm`.
> Meer informatie: <https://github.com/baskerville/bspwm>.

- Definieer twee virtuele bureaubladen:

`bspc monitor {{[-d|--reset-desktops]}} {{1}} {{2}}`

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
