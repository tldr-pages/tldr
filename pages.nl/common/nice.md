# nice

> Voer een programma uit met een aangepaste planningsprioriteit (niceness).
> Niceness-waarden variëren van -20 (de hoogste prioriteit) tot 19 (de laagste).
> Opmerking: sommige moderne planners negeren niceness of beperken de effecten ervan binnen autogroepen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Toon de huidige niceness-waarde:

`nice`

- Verhoog de huidige niceness-waarde met 10:

`nice nice`

- Start een programma met lagere prioriteit:

`nice -{{niceness_waarde}} {{commando}}`

- Start een programma met verhoogde prioriteit:

`sudo nice --{{niceness_waarde}} {{commando}}`

- Definieer de prioriteit met een expliciete optie:

`nice {{[-n|--adjustment]}} {{niceness_waarde}} {{commando}}`
