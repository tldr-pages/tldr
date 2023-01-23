# tldr platform

> A TeX Live platformok kezelése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes elérhető platform listázása a csomagtárban:

`tlmgr platform list`

- Adja hozzá a futtatható fájlokat egy adott platformhoz:

`sudo tlmgr platform add {{platform}}`

- Egy adott platformhoz tartozó futtatható fájlok eltávolítása:

`sudo tlmgr platform remove {{platform}}`

- Automatikus felismerés és váltás az aktuális platformra:

`sudo tlmgr platform set {{auto}}`

- Váltás egy adott platformra:

`sudo tlmgr platform set {{platform}}`
