# magick import

> Leg een deel of het geheel van een X server scherm vast en sla de afbeelding op in een bestand.
> Bekijk ook: `magick`.
> Meer informatie: <https://imagemagick.org/script/import.php>.

- Leg het hele X server scherm vast in een PostScript bestand:

`magick import -window root {{pad/naar/uitvoer.ps}}`

- Leg de inhoud van een extern X server scherm vast in een PNG afbeelding:

`magick import -window root -display {{externe_host}}:{{scherm}}.{{display}} {{pad/naar/uitvoer.png}}`

- Leg een specifiek venster vast op basis van zijn ID zoals weergegeven door `xwininfo` in een JPEG-afbeelding:

`magick import -window {{window_id}} {{pad/naar/uitvoer.jpg}}`
