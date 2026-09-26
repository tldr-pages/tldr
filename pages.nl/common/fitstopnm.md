# fitstopnm

> Converteer een Flexible Image Transport System (FITS) bestand naar een PNM afbeelding.
> Zie ook: `pamtofits`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/fitstopnm.html>.

- Converteer een FITS bestand naar een PNM afbeelding:

`fitstopnm {{pad/naar/bestand.fits}} > {{pad/naar/uitvoer.pnm}}`

- Converteer de afbeelding op de gespecificeerde positie van de derde as in het FITS bestand:

`fitstopnm {{[-i|-image]}} {{z_positie}} {{pad/naar/bestand.fits}} > {{pad/naar/uitvoer.pnm}}`
