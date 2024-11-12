# pamcomp

> Leg twee PAM afbeeldingen over elkaar.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- Leg twee afbeeldingen over elkaar zodat de bovenlaag delen van de onderlaag blokeert:

`pamcomp {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`

- Zet de horizontale uitlijning van de bovenlaag:

`pamcomp -align {{left|center|right|beyondleft|beyondright}} -xoff {{x_offset}} {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`

- Zet de verticale uitlijning van de bovenlaag:

`pamcomp -valign {{top|middle|bottom|above|below}} -yoff {{y_offset}} {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`

- Zet de dekking van de bovenlaag:

`pamcomp -opacity {{0.7}} {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`
