# pamflip

> Flip of draai een PAM of PNM afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Draai de invoer-afbeelding tegen de klok in met de gespecificeerde graden::

`pamflip {{[-r|-rotate]}}{{90|180|270}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Flip links met rechts:

`pamflip {{[-lr|-leftright]}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Flip boven met onder:

`pamflip {{[-tb|-topbottom]}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Flip de invoer-afbeelding met de diagonaal:

`pamflip {{[-xy|-transpose]}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`
