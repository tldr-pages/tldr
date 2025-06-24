# nl

> Voorzie regels van een nummer uit een bestand of van `stdin`.
> Meer informatie: <https://manned.org/nl>.

- Voorzie niet-lege regels in een bestand van een nummer:

`nl {{pad/naar/bestand}}`

- Lees van `stdin`:

`{{commando}} | nl`

- Nummer [a]lle [b]ody regels inclusief lege regels of [n]ummer geen [b]ody regels:

`nl {{[-b|--body-numbering]}} {{a|n}} {{pad/naar/bestand}}`

- Nummer alleen de [b]ody regels die overeenkomen met een basis reguliere expressie (BRE) [p]atroon:

`nl {{[-b|--body-numbering]}} p'FooBar[0-9]' {{pad/naar/bestand}}`

- Gebruik een specifieke [i]ncrement voor regelnummering:

`nl {{[-i|--line-increment]}} {{increment}} {{pad/naar/bestand}}`

- Specificeer het nummeringsformaat voor regels: [r]echts of [l]inks uitgelijnd, met of zonder voorloopnullen ([z]eros):

`nl {{[-n|--number-format]}} {{rz|ln|rn}}`

- Specificeer de breedte ([w]) van de nummering (standaard is 6):

`nl {{[-w|--number-width]}} {{kolombreedte}} {{pad/naar/bestand}}`

- Gebruik een specifieke string om de regelnummers van de regels te [s]cheiden (standaard is TAB):

`nl {{[-s|--number-separator]}} {{scheidingsteken}} {{pad/naar/bestand}}`
