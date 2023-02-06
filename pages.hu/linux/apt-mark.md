# apt-mark

> Segédprogram a telepített csomagok állapotának módosítására. További információ: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Egy csomag automatikus telepítésűként való megjelölése:

`sudo apt-mark auto {{package_name}}`

- Egy csomagot a jelenlegi verziójánál tart, és megakadályozza a frissítéseket:

`sudo apt-mark hold {{package_name}}`

- Engedélyezze egy csomag újbóli frissítését:

`sudo apt-mark unhold {{package_name}}`

- Kézzel telepített csomagok megjelenítése:

`apt-mark showmanual`

- A nem frissített, visszatartott csomagok megjelenítése:

`apt-mark showhold`
