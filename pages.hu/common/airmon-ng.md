# airmon-ng

> A vezeték nélküli hálózati eszközök felügyeleti módjának aktiválása. A `aircrack-ng` weboldal része. További információ: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- A vezeték nélküli eszközök és állapotuk listázása:

`sudo airmon-ng`

- Monitor üzemmód bekapcsolása egy adott eszköz esetében:

`sudo airmon-ng start {{wlan0}}`

- A vezeték nélküli eszközöket használó zavaró folyamatok leállítása:

`sudo airmon-ng check kill`

- Monitor üzemmód kikapcsolása egy adott hálózati interfészhez:

`sudo airmon-ng stop {{wlan0mon}}`
