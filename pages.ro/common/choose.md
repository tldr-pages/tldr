# choose

> O alternativă prietenoasă și rapidă pentru a tăia și (uneori) awk.
> Mai multe informaţii: <https://github.com/theryangeary/choose>

- Imprimați al 5-lea element dintr-o linie (începând de la 0):

`choose {{4}}`

- Imprimați primul, al treilea și al cincilea element dintr-o linie, în care elementele sunt separate prin „:” în loc de spațiu alb:

`choose --field-separator '{{:}}' {{0}} {{2}} {{4}}`

- Imprimați totul, de la al 2-lea la al 5-lea element de pe linie, inclusiv a 5-a:

`choose {{1}}:{{4}}`

- Imprimați totul de la al 2-lea la al 5-lea element de pe linie, excluzând al 5-lea:

`choose --exclusive {{1}}:{{4}}`

- Imprimați începutul liniei la al treilea element:

`choose :{{2}}`

- Imprimați toate elementele de la începutul liniei până la al treilea element (exclusiv):

`choose --exclusive :{{2}}`

- Imprimați toate elementele de la a treia până la sfârșitul liniei:

`choose {{2}}:`

- Imprimați ultimul element dintr-o linie:

`choose {{-1}}`
