# magick convert

> Converteer tussen afbeeldingsformaten, schaal, voeg samen, maak afbeeldingen en nog veel meer.
> Let op: deze tool (voorheen `convert`) is vervangen door `magick` in ImageMagick 7+.
> Meer informatie: <https://imagemagick.org/script/convert.php>.

- Converteer een afbeelding van JPEG naar PNG:

`magick convert {{pad/naar/invoer_afbeelding.jpg}} {{pad/naar/uitvoer_afbeelding.png}}`

- Schaal een afbeelding naar 50% van zijn originele grootte:

`magick convert {{pad/naar/invoer_afbeelding.png}} -resize 50% {{pad/naar/uitvoer_afbeelding.png}}`

- Schaal een afbeelding en behoud de originele aspect ratio tot een maximale dimensie van 640x480:

`magick convert {{pad/naar/invoer_afbeelding.png}} -resize 640x480 {{pad/naar/uitvoer_afbeelding.png}}`

- Schaal een afbeelding zodat deze een gespecificeerde bestandsgrootte heeft:

`magick convert {{pad/naar/invoer_afbeelding.png}} -define jpeg:extent=512kb {{pad/naar/uitvoer_afbeelding.jpg}}`

- Verticaal/horizontaal toevoegen van afbeeldingen:

`magick convert {{pad/naar/afbeelding1.png pad/naar/afbeelding2.png ...}} {{-append|+append}} {{pad/naar/uitvoer_afbeelding.png}}`

- Maak een GIF van een series van afbeeldingen met 100ms pauze ertusen:

`magick convert {{pad/naar/afbeelding1.png pad/naar/afbeelding2.png ...}} -delay {{10}} {{pad/naar/animation.gif}}`

- Maak een afbeelding met niets anders dan een volledig rode achtergrond:

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{pad/naar/afbeelding.png}}`

- Maak een favicon van verschillende afbeeldingen met verschillende groottes:

`magick convert {{pad/naar/afbeelding1.png pad/naar/afbeelding2.png ...}} {{pad/naar/favicon.ico}}`
