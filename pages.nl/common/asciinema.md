# asciinema

> Neemt op en speelt terminal sessies af en deelt hem optioneel op asciinema.org.
> Meer informatie: <https://asciinema.org/docs/usage>.

- Associeer de lokale installatie van `asciinema` met het asciinema.org account:

`asciinema auth`

- Maak een nieuwe opname (gebruiker krijgt een vraag om het lokaal op te slaan of te uploaden als de opname klaar is):

`asciinema rec`

- Maak een nieuwe opname en sla het op in een lokaal bestand:

`asciinema rec {{pad/naar/bestand.cast}}`

- Speelt een terminal opname of vanaf een lokaal bestand:

`asciinema play {{pad/naar/bestand.cast}}`

- Speelt een terminal opname of vanaf asciinema.org:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Maakt een nieuwe opname met een inactieve tijd van maximaal 2,5 seconden:

`asciinema rec -i {{2.5}}`

- Laat de volledige inhoud zien van een lokaal opgeslagen opname:

`asciinema cat {{pad/naar/bestand.cast}}`

- Slaat een lokaal opgeslagen terminal sessie op bij asciinema.org:

`asciinema upload {{pad/naar/bestand.cast}}`
