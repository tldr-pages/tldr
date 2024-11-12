# pngcheck

> Forensische tool voor het valideren van de integriteit van PNG-gebaseerde (PNG, JNG, MNG) afbeeldingsbestanden.
> Kan ook ingebedde afbeeldingen en tekst uit een bestand extraheren.
> Meer informatie: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Controleer de integriteit van een afbeeldingsbestand:

`pngcheck {{pad/naar/bestand.png}}`

- Controleer het bestand met [v]erbeterde en gekleurde ([c]) uitvoer:

`pngcheck -vc {{pad/naar/bestand.png}}`

- Toon de inhoud van [t]ekstfragmenten en zoek ([s]) naar PNG's binnen een specifiek bestand:

`pngcheck -ts {{pad/naar/bestand.png}}`

- Zoek naar en e[x]tracteer ingebedde PNG's binnen een specifiek bestand:

`pngcheck -x {{pad/naar/bestand.png}}`
