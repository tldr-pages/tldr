# asciinema

> Neemt op en speelt terminal sessies af en deelt hem optioneel op asciinema.org.
> Bekijk ook: `terminalizer`.
> Meer informatie: <https://docs.asciinema.org/manual/cli/usage>.

- Associeer de lokale installatie van `asciinema` met het asciinema.org account:

`asciinema auth`

- Maak een nieuwe opname (gebruiker krijgt een vraag om het lokaal op te slaan of te uploaden als de opname klaar is):

`asciinema rec`

- Maak een nieuwe opname en sla het op in een lokaal bestand:

`asciinema rec {{pad/naar/opname.cast}}`

- Speel een terminal opname af vanaf een lokaal bestand:

`asciinema play {{pad/naar/opname.cast}}`

- Speel een terminal opname af vanaf asciinema.org:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Maak een nieuwe opname met een [i]nactieve tijd van maximaal 2,5 seconden:

`asciinema rec -i 2.5`

- Laat de volledige inhoud zien van een lokaal opgeslagen opname:

`asciinema cat {{pad/naar/opname.cast}}`

- Sla een lokaal opgeslagen terminal sessie op bij asciinema.org:

`asciinema upload {{pad/naar/opname.cast}}`
