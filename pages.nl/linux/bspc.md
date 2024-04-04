# bspc

> Een tool om `bspwm` te besturen.
> Meer informatie: <https://github.com/baskerville/bspwm>.

- Definieer twee virtuele bureaubladen:

`bspc monitor --reset-desktops {{1}} {{2}}`

- Focus op het gegeven bureaublad:

`bspc desktop --focus {{number}}`

- Sluit de vensters die afgetakt zijn van het geselecteerde knooppunt:

`bspc node --close`

- Stuur het geselecteerde knooppunt naar het opgegeven bureaublad:

`bspc node --to-desktop {{number}}`

- Schakel de modus volledig scherm in voor het geselecteerde knooppunt:

`bspc node --state ~fullscreen`

- Zet de waarde van een specifieke instelling:

`bspc config {{instelling}} {{waarde}}`
