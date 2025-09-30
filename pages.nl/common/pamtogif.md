# pamtogif

> Converteer een Netpbm afbeelding naar een ongeanimeerde GIF afbeelding.
> Zie ook: `giftopnm`, `gifsicle`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Converteer een Netpbm afbeelding naar een ongeanimeerde GIF afbeelding:

`pamtogif {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.gif}}`

- Markeer de gespecificeerde kleur als transparent in het uitvoer GIF bestand:

`pamtogif {{[-t|-transparent]}} {{kleur}} {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.gif}}`

- Voeg de gespecificeerde tekst toe als commentaar in het uitvoer GIF bestand:

`pamtogif {{[-c|-comment]}} "{{Hallo Wereld!}}" {{pad/naar/afbeelding.pam}} > {{pad/naar/uitvoer.gif}}`
