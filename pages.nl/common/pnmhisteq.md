# pnmhisteq

> Pas histogramequalisatie toe op een PNM afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

- Verhoog het contrast van een PNM afbeelding met behulp van histogramequalisatie:

`pnmhisteq {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Wijzig alleen grijze pixels:

`pnmhisteq {{[-g|-grey]}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`

- Sluit zwarte of witte pixels uit van de histogramequalisatie:

`pnmhisteq -no{{black|white}} {{pad/naar/invoer.pnm}} > {{pad/naar/uitvoer.pnm}}`
