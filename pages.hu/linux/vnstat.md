# vnstat

> Konzol alapú hálózati forgalomfigyelő. További információ: <https://manned.org/vnstat>.

- Az összes interfész forgalmi összefoglalójának megjelenítése:

`vnstat`

- Egy adott hálózati interfész forgalmi összefoglalójának megjelenítése:

`vnstat -i {{eth0}}`

- Élő statisztikák megjelenítése egy adott hálózati interfészhez:

`vnstat -l -i {{eth0}}`

- Az elmúlt 24 óra forgalmi statisztikáinak óránkénti megjelenítése oszlopdiagram segítségével:

`vnstat -hg`

- Az átlagos forgalom mérése és megjelenítése 30 másodpercen keresztül:

`vnstat -tr {{30}}`
