# ethtool

> Hálózati interfészvezérlő (NIC) paramétereinek megjelenítése és módosítása. További információ: <http://man7.org/linux/man-pages/man8/ethtool.8.html>.

- Egy interfész aktuális beállításainak megjelenítése:

`ethtool {{eth0}}`

- Egy interfész illesztőprogram-információinak megjelenítése:

`ethtool --driver {{eth0}}`

- Egy interfész összes támogatott funkciójának megjelenítése:

`ethtool --show-features {{eth0}}`

- Egy interfész hálózathasználati statisztikáinak megjelenítése:

`ethtool --statistics {{eth0}}`

- Egy vagy több LED villogtatása egy interfészen 10 másodpercig:

`ethtool --identify {{eth0}} {{10}}`

- A kapcsolat sebességének, duplex módjának és a paraméterek automatikus egyeztetésének beállítása egy adott interfészhez:

`ethtool -s {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`
