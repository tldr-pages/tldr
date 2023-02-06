# tlmgr option

> TeX Live beállításkezelő. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes TeX Live beállítás listája:

`tlmgr option showall`

- Az összes jelenleg beállított Tex Live-beállítás listázása:

`tlmgr option show`

- Az összes TeX Live beállítás kinyomtatása JSON formátumban:

`tlmgr option showall --json`

- Egy adott TeX Live beállítás értékének megjelenítése:

`tlmgr option {{setting}}`

- Egy adott TeX Live beállítás értékének módosítása:

`tlmgr option {{setting}} {{value}}`

- A TeX Live beállítása, hogy a jövőbeni frissítéseket az internetről kapja a DVD-ről történő telepítés után:

`tlmgr option {{repository}} {{https://mirror.ctan.org/systems/texlive/tlnet}}`
