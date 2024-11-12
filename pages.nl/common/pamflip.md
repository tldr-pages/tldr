# pamflip

> Flip of draai een PAM of PNM afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- Draai de invoer-afbeelding tegen de klok in met de gespecificeerde graden::

`pamflip -rotate{{90|180|270}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Flip links met rechts:

`pamflip -leftright {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Flip boven met onder:

`pamflip -topbottom {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Flip de invoer-afbeelding met de diagonaal:

`pamflip -transpose {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`
