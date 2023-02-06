# tlmgr update

> A TeX Live csomagok frissítése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes TeX Live csomag frissítése:

`sudo tlmgr update --all`

- Frissítse magát a tlmgr-t:

`sudo tlmgr update --self`

- Egy adott csomag frissítése:

`sudo tlmgr update {{package}}`

- Az összes frissítése, kivéve egy adott csomagot:

`sudo tlmgr update --all --exclude {{package}}`

- Az összes csomag frissítése, biztonsági másolat készítése az aktuális csomagokról:

`sudo tlmgr update --all --backup`

- Egy adott csomag frissítése a függőségek frissítése nélkül:

`sudo tlmgr update --no-depends {{package}}`

- Az összes csomag frissítésének szimulálása változtatások nélkül:

`sudo tlmgr update --all --dry-run`
