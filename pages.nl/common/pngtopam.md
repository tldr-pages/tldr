# pngtopam

> Converteer een PNG afbeelding naar een Netpbm afbeelding.
> Bekijk ook: `pamtopng`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

- Converteer de gespecificeerde PNG afbeelding naar een Netpbm afbeelding:

`pngtopam {{pad/naar/afbeelding.png}} > {{pad/naar/uitvoer.pam}}`

- Maak een uitvoerafbeelding die zowel de hoofdafbeelding als de transparantiemasker van de invoerafbeelding bevat:

`pngtopam -alphapam {{pad/naar/afbeelding.png}} > {{pad/naar/uitvoer.pam}}`

- Vervang transparente pixels door de gespecificeerde kleur:

`pngtopam -mix -background {{kleur}} {{pad/naar/afbeelding.png}} > {{pad/naar/uitvoer.pam}}`

- Schrijf tEXt chunks gevonden in de invoer-afbeelding naar het gespecificeerde tekstbestand:

`pngtopam -text {{pad/naar/bestand.txt}} {{pad/naar/afbeelding.png}} > {{pad/naar/uitvoer.pam}}`
