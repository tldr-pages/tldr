# pamfunc

> Pas een eenvoudige rekenkundige functie toe op een Netpbm afbeelding.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamfunc.html>.

- Pas de gespecificeerde rekenkundige functie toe met `n` als tweede argument op elk sample in de gespecificeerde PAM afbeelding:

`pamfunc -{{multiplier|divisor|adder|subtractor|min|max}} {{n}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`

- Pas de gespecificeerde bitstring-functie toe met `n` als tweede argument op elk sample in de gespecificeerde PAM afbeelding:

`pamfunc -{{andmask|ormask|xormask|shiftleft|shiftright}} {{n}} {{pad/naar/invoer.pam}} > {{pad/naar/uitvoer.pam}}`
