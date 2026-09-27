# qalc

> Krachtige en gebruiksvriendelijke rekenmachine.
> Zie ook: `bc`.
> Meer informatie: <https://qalculate.github.io/manual/qalc.html>.

- Start in interactieve modus:

`qalc {{[-i|--interactive]}}`

- Start in beknopte modus (toon alleen de resultaten):

`qalc {{[-t|--terse]}}`

- Update wisselkoersen:

`qalc {{[-e|--exrates]}}`

- Voer berekeningen niet-interactief uit:

`qalc {{66+99|2^4|6 feet to cm|1 bitcoin to USD|20 kmph to mph|...}}`

- Toon alle ondersteunde functies/prefixen/eenheden/variabelen:

`qalc --{{list-functions|list-prefixes|list-units|list-variables}}`

- Voer commando's uit vanuit een bestand:

`qalc {{[-f|--file]}} {{pad/naar/bestand}}`
