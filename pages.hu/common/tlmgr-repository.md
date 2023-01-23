# tlmgr repository

> A TeX Live telepítés tárolóinak kezelése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes konfigurált tárolóhely és azok címkéinek (ha be van állítva) listázása:

`tlmgr repository list`

- Egy adott tárolóban elérhető összes csomag listázása:

`tlmgr repository list {{path|url|tag}}`

- Új tároló hozzáadása egy adott címkével (a címke nem kötelező):

`sudo tlmgr repository add {{path|url}} {{tag}}`

- Egy adott tároló eltávolítása:

`sudo tlmgr repository remove {{path|url|tag}}`

- A tárolók új listájának beállítása, felülírva az előző listát:

`sudo tlmgr repository set {{path|url|tag}}#{{tag}} {{path|url|tag}}#{{tag}} {{...}}`

- Az összes beállított adattár ellenőrzési státuszának megjelenítése:

`tlmgr repository status`
