# unzip

> Extraheer bestanden/mappen van Zip-archieven.
> Zie ook: `zip`.
> Meer informatie: <https://manned.org/unzip>.

- Extraheer alle bestanden/mappen van een specifiek archief naar de huidige map:

`unzip {{pad/naar/archief}}.zip`

- Extraheer bestanden/mappen van een archief naar een specifieke map:

`unzip {{pad/naar/archief}}.zip -d {{pad/naar/uitvoer}}`

- Extraheer bestanden/mappen van een archief naar `stdout` naast de geëxtraheerde bestandsnamen:

`unzip -c {{pad/naar/archief}}.zip`

- Extraheer een archief dat gemaakt is op Windows, dat bestanden bevat met niet-ASCII (bijv. Chinese of Japanse tekens) bestandsnamen:

`unzip -O {{gbk}} {{pad/naar/archief}}.zip`

- Toon de inhoud van een specifiek archief zonder te extraheren:

`unzip -l {{pad/naar/archief}}.zip`

- Extraheer specifieke bestanden uit een archief naar de huidige map, waarbij mappaden worden genegeerd:

`unzip -j {{pad/naar/archief}}.zip {{pad/naar/bestand1_in_archief pad/naar/bestand2_in_archief ...}}`
