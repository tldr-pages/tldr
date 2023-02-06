# tlmgr paper

> A TeX Live telepítés papírméret beállításainak kezelése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes TeX Live program által használt alapértelmezett papírméret megjelenítése:

`tlmgr paper`

- Állítsa be az összes TeX Live program alapértelmezett papírméretét A4-re:

`sudo tlmgr paper {{a4}}`

- Egy adott TeX Live program által használt alapértelmezett papírméret megjelenítése:

`tlmgr {{pdftex}} paper`

- Egy adott TeX Live program alapértelmezett papírméretének beállítása A4-re:

`sudo tlmgr {{pdftex}} paper {{a4}}`

- Egy adott TeX Live program összes elérhető papírméretének felsorolása:

`tlmgr {{pdftex}} paper --list`

- Az összes TeX Live program által használt alapértelmezett papírméret kiürítése JSON formátumban:

`tlmgr paper --json`
