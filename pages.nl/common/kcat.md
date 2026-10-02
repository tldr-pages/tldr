# kcat

> Apache Kafka producer- en consumenttool.
> Meer informatie: <https://manned.org/kcat>.

- Consumeer berichten startend met de nieuwste offset:

`kcat -C -t {{onderwerp}} -b {{brokers}}`

- Consumeer berichten startend met de oudste offset en sluit af nadat het laatste bericht is ontvangen:

`kcat -C -t {{onderwerp}} -b {{brokers}} -o beginning -e`

- Consumeer berichten als een Kafka-consumentgroep:

`kcat -G {{groep_id}} {{onderwerp}} -b {{brokers}}`

- Publiceer bericht via het lezen van de `stdin`:

`echo {{bericht}} | kcat -P -t {{onderwerp}} -b {{brokers}}`

- Publiceer berichten via het lezen van een bestand:

`kcat -P -t {{onderwerp}} -b {{brokers}} {{pad/naar/bestand}}`

- Toon de metadata voor alle onderwerpen en brokers:

`kcat -L -b {{brokers}}`

- Toon de metadata voor een specifiek onderwerp:

`kcat -L -t {{onderwerp}} -b {{brokers}}`

- Verkrijg de offset voor een onderwerp/partitie voor een specifiek punt in de tijd:

`kcat -Q -t {{onderwerp}}:{{partitie}}:{{unix_timestamp}} -b {{brokers}}`
