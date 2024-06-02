# pamcut

> Snij een rechthoekig gebied uit van een Netpbm afbeelding.
> Bekijk ook: `pamcrop`, `pamdice`, `pamcomp`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Verwijder het gespecificeerde nummer van kolommen/rijen van iedere zijde van de afbeelding:

`pamcut -cropleft {{waarde}} -cropright {{waarde}} -croptop {{waarde}} -cropbottom {{waarde}} {{pad/naar/afbeelding.ppm}} > {{pad/naar/uitvoer.ppm}}`

- Behoud alleen de kolommen tussen de gespecificeerde kolommen (inclusief de gespecificeerde):

`pamcut -left {{waarde}} -right {{waarde}} {{pad/naar/afbeelding.ppm}} > {{pad/naar/uitvoer.ppm}}`

- Vul missende gebieden met zwarte pixels als de gespecificeerde rechthoek niet volledig ligt in de invoer-afbeelding:

`pamcut -top {{waarde}} -bottom {{waarde}} -pad {{pad/naar/afbeelding.ppm}} > {{pad/naar/uitvoer.ppm}}`
