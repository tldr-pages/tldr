# pamtotiff

> Converteer een PAM afbeelding naar een TIFF bestand.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

- Converteer een PAM afbeelding naar een TIFF afbeelding:

`pamtotiff {{pad/naar/invoer_bestand.pam}} > {{pad/naar/uitvoer_bestand.tiff}}`

- Specificeer expliciet de compressie methode voor een uitvoerbestand:

`pamtotiff -{{none|packbits|lzw|g3|g4|flate|adobeflate}} {{pad/naar/invoer_bestand.pam}} > {{pad/naar/uitvoer_bestand.tiff}}`

- Produceer altijd een gekleurde TIFF afbeelding, ook als de invoer afbeelding een grijsschaal is:

`pamtotiff -color {{pad/naar/invoer_bestand.pam}} > {{pad/naar/uitvoer_bestand.tiff}}`
