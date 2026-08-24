# unzip

> Extraheer bestanden/mappen van Zip-archieven.
> Zie ook: `zip`.
> Meer informatie: <https://manned.org/unzip>.

- Extraheer alle bestanden/mappen van specifieke archieven naar de huidige map:

`unzip {{pad/naar/archief1.zip pad/naar/archief2.zip ...}}`

- Extraheer bestanden/mappen van archieven naar een specifiek pad:

`unzip {{pad/naar/archief1.zip pad/naar/archief2.zip ...}} -d {{pad/naar/uitvoer}}`

- Extraheer bestanden/mappen van archieven naar `stdout` naast de geëxtraheerde bestandsnamen:

`unzip -c {{pad/naar/archief1.zip pad/naar/archief2.zip ...}}`

- Extraheer een archief dat gemaakt is op Windows, die bestanden bevat met niet-ASCII (bijv. Chinese of Japanse tekens) bestandsnamen:

`unzip -O {{gbk}} {{pad/naar/archief1.zip pad/naar/archief2.zip ...}}`

- Toon de inhoud van specifiek archief zonder te extraheren:

`unzip -l {{pad/naar/archief}}.zip`

- Extraheer specifieke bestanden uit een archief:

`unzip -j {{pad/naar/archief}}.zip {{pad/naar/bestand1_in_archief pad/naar/bestand2_in_archief ...}}`
