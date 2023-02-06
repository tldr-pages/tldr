# iotop

> A folyamatok vagy szálak aktuális I/O-használatának táblázata. További információ: <https://manned.org/iotop>.

- A top-like I/O monitor elindítása:

`sudo iotop`

- Csak a ténylegesen I/O-t végző folyamatok vagy szálak megjelenítése:

`sudo iotop --only`

- Az I/O-használat megjelenítése nem interaktív módban:

`sudo iotop --batch`

- Csak a folyamatok I/O-használatának megjelenítése (alapértelmezett az összes szál megjelenítése):

`sudo iotop --processes`

- Adott PID(s) I/O-használatának megjelenítése:

`sudo iotop --pid={{PID}}`

- Adott felhasználó I/O-használatának megjelenítése:

`sudo iotop --user={{user}}`

- Sávszélesség helyett a felhalmozott I/O megjelenítése:

`sudo iotop --accumulated`
