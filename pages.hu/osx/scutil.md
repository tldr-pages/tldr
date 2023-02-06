# scutil

> Rendszerkonfigurációs paraméterek kezelése. A konfiguráció beállításához szükséges, hogy a rendszergazda legyen. További információ: <https://ss64.com/osx/scutil.html>.

- DNS konfiguráció megjelenítése:

`scutil --dns`

- A proxy konfiguráció megjelenítése:

`scutil --proxy`

- Számítógép nevének lekérdezése:

`scutil --get ComputerName`

- Számítógépnév beállítása:

`sudo scutil --set ComputerName {{computer_name}}`

- Hostnév lekérdezése:

`scutil --get HostName`

- Hostnév beállítása:

`scutil --set HostName {{hostname}}`
