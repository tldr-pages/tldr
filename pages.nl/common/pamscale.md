# pamscale

> Schaal een Netpbm afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamscale.html>.

- Schaal een afbeelding zodat het resultaat de gespecificeerde verhoudingen heeft:

`pamscale -width {{breedte}} -height {{hoogte}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoering.pam}}`

- Schaal een afbeelding zodat het resultaat de gespecificeerde breedte heeft met behoud van de beeldverhouding:

`pamscale -width {{breedte}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Schaal een afbeelding zodat de breedte en de hoogte aangepast worden volgens de gespecificeerde factoren:

`pamscale -xscale {{x_factor}} -yscale {{y_factor}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Schaal een afbeelding zodat het past binnen het kader met behoud van de beeldverhouding:

`pamscale -xyfit {{kader_breedte}} {{kader_hoogte}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Schaal een afbeelding zodat het de gespecificeerde rechthoek volledig vult met behoud van de beeldverhouding:

`pamscale -xyfill {{rechthoek_breedte}} {{rechthoek_hoogte}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`
