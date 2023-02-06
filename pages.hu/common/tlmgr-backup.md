# tlmgr backup

> A TeX Live csomagok biztonsági másolatainak kezelése. Az alapértelmezett biztonsági másolat könyvtárát a `backupdir` opció adja meg, és a `tlmgr option` kapcsolóval érhető el. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Biztonsági mentés készítése egy vagy több csomagról:

`tlmgr backup {{package1 package2 ...}}`

- Biztonsági mentés készítése az összes csomagról:

`tlmgr backup --all`

- Biztonsági mentés készítése egy egyéni könyvtárba:

`tlmgr backup {{package}} --backupdir {{path/to/backup_directory}}`

- Egy vagy több csomag biztonsági mentésének eltávolítása:

`tlmgr backup clean {{package1 package2 ...}}`

- Az összes biztonsági mentés eltávolítása:

`tlmgr backup clean --all`
