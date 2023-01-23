# tlmgr remove

> A TeX Live csomagok eltávolítása. Alapértelmezés szerint az eltávolított csomagok biztonsági mentést kapnak a `./tlpkg/backups` címre a TL telepítési könyvtárában. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Egy TeX Live csomag eltávolítása:

`sudo tlmgr remove {{package}}`

- Egy csomag eltávolításának szimulálása változtatások nélkül:

`tlmgr remove --dry-run {{package}}`

- Egy csomag eltávolítása a függőségek nélkül:

`sudo tlmgr remove --no-depends {{package}}`

- Egy csomag eltávolítása és biztonsági mentés egy adott könyvtárba:

`sudo tlmgr remove --backupdir {{path/to/directory}} {{package}}`

- Az egész TeX Live eltávolítása, megerősítést kérve:

`sudo tlmgr remove --all`
