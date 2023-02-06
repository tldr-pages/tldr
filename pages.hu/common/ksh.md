# ksh

> Korn Shell, egy Bash-kompatibilis parancssor-értelmező. Lásd még: `histexpand`. További információ: <http://kornshell.com>.

- Indítson el egy interaktív shell munkamenetet:

`ksh`

- Konkrét \[c\]ommandók végrehajtása:

`ksh -c "{{echo 'ksh is executed'}}"`

- Egy adott szkript végrehajtása:

`ksh {{path/to/script.ksh}}`

- Egy adott szkript ellenőrzése szintaktikai hibák szempontjából anélkül, hogy végrehajtaná azt:

`ksh -n {{path/to/script.ksh}}`

- Egy adott szkript végrehajtása, a szkript minden egyes parancsának kinyomtatása a végrehajtás előtt:

`ksh -x {{path/to/script.ksh}}`
