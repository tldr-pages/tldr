# roll

> Rolls o secvență de zaruri definite de utilizator.

- Roll 3 zaruri cu 6 fețe și însumează rezultatele:

`roll {{3d}}`

- Roll 1 8 fețe mor, se adaugă 3 și se însumează rezultatele:

`roll {{d8 + 3}}`

- Rulați 4 zaruri cu 6 fețe, păstrați cele mai mari 3 rezultate și însumați rezultatele:

`roll {{4d6h3}}`

- Roll 2 12 zaruri laterale de 2 ori și arată fiecare rolă:

`roll --verbose {{2{2d12}}}`

- Rotiți 2 zaruri 20 de fețe până când rezultatul este mai mare de 10:

`roll "{{2d20>10}}"`

- Roll 2 zaruri 5 fețe de 3 ori și arată suma totală:

`roll --sum-series {{3{2d5}}}`
