# asciinema

> Neemt op en speelt terminal sessies af en deelt hem optioneel op asciinema.org.
> Zie ook: `terminalizer`.
> Meer informatie: <https://docs.asciinema.org/manual/cli/>.

- Associeer de lokale installatie van `asciinema` met het asciinema.org account:

`asciinema {{[a|auth]}}`

- Maak een nieuwe opname en sla het op in een lokaal bestand (sluit het af met `<Ctrl d>` of typ `exit`):

`asciinema {{[r|record]}} {{pad/naar/opname.cast}}`

- Speel een terminal opname af vanaf een lokaal bestand:

`asciinema {{[p|play]}} {{pad/naar/opname.cast}}`

- Speel een terminal opname af vanaf asciinema.org:

`asciinema {{[p|play]}} https://asciinema.org/a/{{cast_id}}`

- Maak een nieuwe opname met een inactieve tijd van maximaal 2,5 seconden:

`asciinema {{[r|record]}} {{[-i|--idle-time-limit]}} 2.5`

- Laat de volledige inhoud zien van een lokaal opgeslagen opname:

`asciinema {{[ca|cat]}} {{pad/naar/opname.cast}}`

- Sla een lokaal opgeslagen terminal sessie op bij asciinema.org:

`asciinema {{[u|upload]}} {{pad/naar/opname.cast}}`

- Stream de huidige terminal op een lokale webpagina:

`asciinema {{[st|stream]}} --local`
