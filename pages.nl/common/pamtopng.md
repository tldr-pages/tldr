# pamtopng

> Converteer een PAM afbeelding naar PNG.
> Bekijk ook: `pnmtopng`, `pngtopam`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamtopng.html>.

- Converteer de gespecificeerde PAM afbeelding naar PNG:

`pamtopng {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.png}}`

- Markeer de gespecificeerde kleur als transparent in de uitvoer-afbeelding:

`pamtopng -transparent {{kleur}} {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.png}}`

- Voeg de tekst in gespecificeerde bestand toe als tEXt chunks in de uitvoer:

`pamtopng -text {{pad/naar/bestand.txt}} {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.png}}`

- Zorg ervoor dat het uitvoerbestand geïnterlaced is in Adam7-formaat:

`pamtopng -interlace {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.png}}`
