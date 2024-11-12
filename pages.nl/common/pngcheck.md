# pngcheck

> Gedetailleerde informatie over en verifiëren van PNG-, JNG- en MNG-bestanden.
> Meer informatie: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Toon een samenvatting van een afbeelding (breedte, hoogte, en kleurdiepte):

`pngcheck {{pad/naar/afbeelding.png}}`

- Toon informatie over een afbeelding met gekleurde ([c]) uitvoer:

`pngcheck -c {{pad/naar/afbeelding.png}}`

- Toon gedetailleerde ([v]) informatie over een afbeelding:

`pngcheck -cvt {{pad/naar/afbeelding.png}}`

- Ontvang een afbeelding van `stdin` en toon gedetailleerde informatie:

`cat {{pad/naar/afbeelding.png}} | pngcheck -cvt`

- Zoek ([s]) naar PNG-bestanden binnen een specifiek bestand en toon informatie:

`pngcheck -s {{pad/naar/afbeelding.png}}`

- Zoek naar PNG's binnen een ander bestand en e[x]tracteer ze:

`pngcheck -x {{pad/naar/afbeelding.png}}`
