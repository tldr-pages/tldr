# dc

> Een rekenmachine met willekeurige precisie. Gebruikt reverse polish notation (RPN).
> Zie ook: `bc`, `qalc`.
> Meer informatie: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>.

- Start een interactieve sessie:

`dc`

- Voer een script uit:

`dc {{pad/naar/script.dc}}`

- Bereken een uitdrukking met de gespecificeerde schaal:

`dc {{[-e|--expression]}} '{{10}} k {{5 3 /}} p'`

- Bereken 4 keer 5 (4 5 *), trek er 17 vanaf (17 -), en [p]rint de uitvoer:

`dc {{[-e|--expression]}} '4 5 * 17 - p'`

- Specificeer het aantal decimalen op 7 (7 k), bereken 5 gedeeld door -3 (5 _3 /) en [p]rint:

`dc {{[-e|--expression]}} '7 k 5 _3 / p'`

- Bereken de gulden snede, phi: stel het aantal decimalen in op 100 (100 k), wortel van 5 (5 v) plus 1 (1 +), gedeeld door 2 (2 /), en [p]rint het resultaat:

`dc {{[-e|--expression]}} '100 k 5 v 1 + 2 / p'`
