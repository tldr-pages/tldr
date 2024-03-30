# kcat

> Apache Kafka produceer en consumeer tool.
> Meer informatie: <https://github.com/edenhill/kcat>.

- Consumeer berichten startend met de nieuwste offset:

`kcat -C -t {{onderwerp}} -b {{makelaars}}`

- Consumeer berichten startend met de oudste offset en sluit af nadat het laatste bericht is ontvangen:

`kcat -C -t {{onderwerp}} -b {{makelaars}} -o beginning -e`

- Consumeer berichten als een Kafka consumeer groep:

`kcat -G {{groep_id}} {{onderwerp}} -b {{makelaars}}`

- Publiceer bericht via het lezen van de `stdin`:

`echo {{bericht}} | kcat -P -t {{onderwerp}} -b {{makelaars}}`

- Publiceer berichten via het lezen van een bestand:

`kcat -P -t {{onderwerp}} -b {{makelaars}} {{pad/naar/bestand}}`

- Toon de metadata voor alle onderwerpen en makelaars:

`kcat -L -b {{makelaars}}`

- Toon de metadata voor een specifiek onderwerp:

`kcat -L -t {{onderwerp}} -b {{makelaars}}`

- Verkrijg de offset voor een onderwerp/partitie voor een specifiek punt in de tijd:

`kcat -Q -t {{onderwerp}}:{{partitie}}:{{unix_timestamp}} -b {{makelaars}}`
