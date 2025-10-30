# sfdisk

> Toon of manipuleer een schijfpartitietabel.
> Meer informatie: <https://manned.org/sfdisk>.

- Sla een backup van de partitie-indeling op naar een bestand:

`sudo sfdisk {{[-d|--dump]}} {{/dev/sdX}} > {{pad/naar/bestand.dump}}`

- Herstel een partitie-indeling:

`sudo sfdisk < {{pad/naar/bestand.dump}} {{/dev/sdX}}`

- Stel het partitietype in:

`sudo sfdisk --part-type {{/dev/sdX}} {{partitie_nummer}} {{swap}}`

- Verwijder een partitie:

`sudo sfdisk --delete {{/dev/sdX}} {{partitie_nummer}}`

- Toon de help:

`sfdisk {{[-h|--help]}}`
