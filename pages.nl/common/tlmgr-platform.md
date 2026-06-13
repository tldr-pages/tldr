# tlmgr platform

> Beheer TeX Live platforms.
> Meer informatie: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

- Toon alle beschikbare platforms in een pakket repository:

`tlmgr {{[arch|platform]}} list`

- Voeg de uitvoerbare bestanden toe aan een specifiek platform:

`sudo tlmgr {{[arch|platform]}} add {{platform}}`

- Verwijder de uitvoerbare bestanden uit een specifiek platform:

`sudo tlmgr {{[arch|platform]}} remove {{platform}}`

- Detecteer automatisch en wissel naar het huidige platform:

`sudo tlmgr {{[arch|platform]}} set auto`

- Wissel naar een specifiek platform:

`sudo tlmgr {{[arch|platform]}} set {{platform}}`
