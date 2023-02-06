# path

> A végrehajtható fájlok keresési útvonalának megjelenítése vagy beállítása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- Az aktuális elérési útvonal megjelenítése:

`path`

- Az elérési útvonal beállítása egy vagy több pontosvesszővel elválasztott könyvtárhoz:

`path {{path/to/directory(s)}}`

- Új könyvtár hozzáadása az eredeti elérési útvonalhoz:

`path {{path/to/directory}};%path%`

- Parancssor beállítása, hogy csak az aktuális könyvtárban keressen futtatható fájlokat:

`path ;`
