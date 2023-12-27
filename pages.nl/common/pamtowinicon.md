# pamtowinicon

> Converteer een PAM afbeelding naar een Windows ICO bestand.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamtowinicon.html>.

- Converteer een PAM afbeelding naar een ICO bestand:

`pamtowinicon {{pad/naar/invoer_bestand.pam}} > {{pad/naar/uitvoer.ico}}`

- Encodeer afbeeldingen met resoluties kleiner dan t in het BMP formaat en alle andere afbeeldingen in het PNG formaat:

`pamtowinicon -pngthreshold {{t}} {{pad/naar/invoer_bestand.pam}} > {{pad/naar/uitvoer.ico}}`

- Maak alle pixels buiten het doorzichtige vlak zwart:

`pamtowinicon -truetransparent {{pad/naar/invoer_bestand.pam}} > {{pad/naar/uitvoer.ico}}`
