# tlmgr platform

> Beheer TeX Live platforms.
> Meer informatie: <https://www.tug.org/texlive/tlmgr.html>.

- Toon alle beschikbare platforms in een pakket repository:

`tlmgr platform list`

- Voeg de uitvoerbare bestanden toe aan een specifiek platform:

`sudo tlmgr platform add {{platform}}`

- Verwijder de uitvoerbare bestanden uit een specifiek platform:

`sudo tlmgr platform remove {{platform}}`

- Detecteer automatisch en wissel naar het huidige platform:

`sudo tlmgr platform set auto`

- Wissel naar een specifiek platform:

`sudo tlmgr platform set {{platform}}`
