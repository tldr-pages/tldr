# zgrep

> Zoek tekstpatronen in bestanden binnen gecomprimeerde bestanden.
> Meer informatie: <https://manned.org/zgrep>.

- Zoek een patroon in een gecomprimeerd bestand (hoofdlettergevoelig):

`zgrep {{patroon}} {{pad/naar/gecomprimeerd_bestand}}`

- Toon 3 regels rondom [C]ontext, voor ([B]) of  na ([A]) elke overeenkomst:

`zgrep {{--context|--before-context|--after-context}} 3 {{patroon}} {{pad/naar/gecomprimeerd_bestand}}`

- Zoek een patroon in een gecomprimeerd bestand (hoofdletterongevoelig):

`zgrep {{[-i|--ignore-case]}} {{patroon}} {{pad/naar/gecomprimeerd_bestand}}`

- Geef  het aantal regels met het gevonden patroon in een gecomprimeerd bestand weer:

`zgrep {{[-c|--count]}} {{patroon}} {{pad/naar/gecomprimeerd_bestand}}`

- Geef de regels weer waarin het patroon niet voorkomt (de zoekfunctie omkeren):

`zgrep {{[-v|--invert-match]}} {{patroon}} {{pad/naar/gecomprimeerd_bestand}}`

- Zoek in een gecomprimeerd bestand naar meerdere patronen:

`zgrep {{[-e|--regexp]}} "{{patroon_1}}" {{[-e|--regexp]}} "{{patroon_2}}" {{pad/naar/gecomprimeerd_bestand}}`

- Gebruik uitgebreide `regex` (ondersteunt `?`, `+`, `{}`, `()` en `|`):

`zgrep {{[-E|--extended-regexp]}} {{regex}} {{pad/naar/bestand}}`
