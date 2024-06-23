# bspc

> Een tool om `bspwm` te besturen.
> Meer informatie: <https://github.com/baskerville/bspwm>.

- Definieer twee virtuele bureaubladen:

`bspc monitor --reset-desktops {{1}} {{2}}`

- Focus op het gegeven bureaublad:

`bspc desktop --focus {{nummer}}`

- Sluit de vensters die afgetakt zijn van de geselecteerde node:

`bspc node --close`

- Stuur de geselecteerde node naar het opgegeven bureaublad:

`bspc node --to-desktop {{nummer}}`

- Schakel de modus volledig scherm in voor de geselecteerde node:

`bspc node --state ~fullscreen`

- Zet de waarde van een specifieke instelling:

`bspc config {{instelling}} {{waarde}}`
