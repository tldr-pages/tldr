# sleep

> Wacht voor een gespecificeerde hoeveelheid tijd.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- Wacht in seconden:

`sleep {{seconden}}`

- Wacht in [m]inuten. (Andere eenheden zoals [d]ag, [u]ur, [s]econde, [inf]initeit kunnen ook worden gebruikt):

`sleep {{minuten}}m`

- Wacht 1 [d]ag en 3 uur ([h]):

`sleep 1d 3h`

- Voer een specifiek commando uit na een wachttijd van 20 [m]inuten:

`sleep 20m && {{commando}}`

- Wacht voor altijd:

`sleep {{[inf|infinity]}}`

- Toon de help:

`sleep --help`
