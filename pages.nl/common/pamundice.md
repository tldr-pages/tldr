# pamundice

> Combineer een raster van Netpbm afbeeldingen tot één afbeelding.
> Zie ook: `pamdice`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamundice.html>.

- Combineer de afbeeldingen waarvan de namen overeenkomen met de `printf`-stijl bestandsnaam-expressie. Ga uit van een raster met een specifieke afmeting:

`pamundice {{bestandsnaam_%1d_%1a.ppm}} {{[-a|-across]}} {{raster_breedte}} {{[-d|-down]}} {{raster_hoogte}} > {{pad/naar/uitvoer.ppm}}`

- Ga ervan uit dat de tegels horizontaal en verticaal overlappen met het gespecificeerde bedrag:

`pamundice {{bestandsnaam_%1d_%1a.ppm}} {{[-a|-across]}} {{x_waarde}} {{[-d|-down]}} {{y_waarde}} {{[-ho|-hoverlap]}} {{waarde}} {{[-vo|-voverlap]}} {{waarde}} > {{pad/naar/uitvoer.ppm}}`

- Specificeer de te combineren afbeeldingen via een tekstbestand met één bestandsnaam per regel:

`pamundice {{[-l|-listfile]}} {{pad/naar/bestand.txt}} {{[-a|-across]}} {{x_waarde}} {{[-d|-down]}} {{y_waarde}} > {{pad/naar/uitvoer.ppm}}`
