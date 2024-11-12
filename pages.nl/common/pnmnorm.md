# pnmnorm

> Normaliseer het contrast in een PNM afbeelding.
> Bekijk ook: `pnmhisteq`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- Forceer de helderste pixels om wit te zijn, de donkerste pixels om zwart te zijn en verspreid de tussenliggende pixels lineair:

`pnmnorm {{pad/naar/afbeelding.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Forceer de helderste pixels om wit te zijn, de donkerste pixels om zwart te zijn en verspreid de tussenliggende pixels kwadratisch zodat pixels met een helderheid van `n` 50% helderder worden:

`pnmnorm -midvalue {{n}} {{pad/naar/afbeelding.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Behoud de tint van de pixels, pas alleen de helderheid aan:

`pnmnorm -keephues {{pad/naar/afbeelding.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Specificeer een methode om de helderheid van een pixel te berekenen:

`pnmnorm -{{luminosity|colorvalue|saturation}} {{pad/naar/afbeelding.pnm}} > {{pad/naar/uitvoer.pnm}}`
