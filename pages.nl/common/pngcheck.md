# pngcheck

> Forensics tool voor het valideren van de integriteit van PNG-gebaseerde (PNG, JNG, MNG) afbeeldingbestanden.
> Kan ook embedded afbeeldingen en tekst van een bestand extraheren.
> Meer informatie: <https://manned.org/pngcheck>.

- Verifieer de integriteit van een afbeeldingsbestand (breedte, hoogte, en kleurdiepte):

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
