# nice

> Voer een programma uit met een aangepaste planningsprioriteit (niceness).
> Niceness-waarden variëren van -20 (de hoogste prioriteit) tot 19 (de laagste).
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Start een programma met een aangepaste prioriteit:

`nice -{{niceness_waarde}} {{commando}}`

- Definieer de prioriteit met een expliciete optie:

`nice {{[-n|--adjustment]}} {{niceness_waarde}} {{commando}}`
