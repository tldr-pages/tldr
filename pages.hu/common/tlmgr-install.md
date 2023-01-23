# tlmgr install

> A TeX Live csomagok telepítése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Telepítsen egy csomagot és függőségeit:

`sudo tlmgr install {{package}}`

- Egy csomag újratelepítése:

`sudo tlmgr install --reinstall {{package}}`

- Egy csomag telepítésének szimulálása változtatások nélkül:

`tlmgr install --dry-run {{package}}`

- Egy csomag telepítése a függőségek nélkül:

`sudo tlmgr install --no-depends {{package}}`

- Csomag telepítése egy adott fájlból:

`sudo tlmgr install --file {{path/to/package}}`
