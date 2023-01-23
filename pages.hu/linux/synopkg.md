# synopkg

> Csomagkezelő segédprogram a Synology DiskStation Manager számára. További információ: <https://www.synology.com/dsm>.

- A telepített csomagok neveinek listája:

`synopkg list --name`

- Az adott csomagtól függő csomagok listázása:

`synopkg list --depend-on {{package}}`

- Egy csomag indítása/leállítása:

`sudo synopkg {{start|stop}} {{package}}`

- Egy csomag állapotának kinyomtatása:

`synopkg status {{package}}`

- Egy csomag eltávolítása:

`sudo synopkg uninstall {{package}}`

- Ellenőrizze, hogy elérhetőek-e frissítések egy csomaghoz:

`synopkg checkupdate {{package}}`

- Az összes csomag frissítése a legújabb verzióra:

`sudo synopkg upgradeall`

- Csomag telepítése synopkg fájlból:

`sudo synopkg install {{path/to/package.spk}}`
