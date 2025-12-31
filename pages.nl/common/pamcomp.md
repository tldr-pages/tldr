# pamcomp

> Leg twee PAM afbeeldingen over elkaar.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamcomp.html>.

- Leg twee afbeeldingen over elkaar zodat de bovenlaag delen van de onderlaag blokeert:

`pamcomp {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`

- Zet de horizontale uitlijning van de bovenlaag:

`pamcomp {{[-ali|-align]}} {{left|center|right|beyondleft|beyondright}} {{[-x|-xoff]}} {{x_offset}} {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`

- Zet de verticale uitlijning van de bovenlaag:

`pamcomp {{[-va|-valign]}} {{top|middle|bottom|above|below}} {{[-y|-yoff]}} {{y_offset}} {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`

- Zet de dekking van de bovenlaag:

`pamcomp {{[-o|-opacity]}} {{0.7}} {{pad/naar/bovenlaag.pam}} {{pad/naar/onderlaag.pam}} > {{pad/naar/uitvoer.pam}}`
