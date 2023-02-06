# tlmgr restore

> A `tlmgr backup` opcióval létrehozott csomagmentések visszaállítása. Az alapértelmezett mentési könyvtárat a `backupdir` opció adja meg, és a `tlmgr option` opcióval kapható meg. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Az összes elérhető biztonsági mentés revízióinak listázása az összes csomaghoz:

`tlmgr restore`

- Egy adott csomag összes elérhető biztonsági másolat-felülvizsgálatának listázása:

`tlmgr restore {{package}}`

- Egy adott csomag egy adott revíziójának visszaállítása:

`tlmgr restore {{package}} {{revision}}`

- Az összes mentett csomag legutóbbi revíziójának visszaállítása:

`tlmgr restore --all`

- Csomag visszaállítása egyéni biztonsági mentési könyvtárból:

`tlmgr restore {{package}} {{revision}} --backupdir {{path/to/backup_directory}}`

- Szárazfutás végrehajtása és az összes elvégzett művelet kinyomtatása anélkül, hogy elvégezné azokat:

`tlmgr restore --dry-run {{package}} {{revision}}`
