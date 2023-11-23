# cmp

> Vergelijk twee bestanden byte voor byte.
> Meer informatie: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Toon karakter en regelnummer van het eerste verschil tussen twee bestanden:

`cmp {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Toon info van het eerste verschil: karakter, regelnummer, bytes en waardes:

`cmp --print-bytes {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Toon de byte nummers en waardes van ieder verschil:

`cmp --verbose {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Vergelijk bestanden, maar toon niets, pak alleen de exit status:

`cmp --quiet {{pad/naar/bestand1}} {{pad/naar/bestand2}}`
