# iwconfig

> Egy vezeték nélküli hálózati interfész paramétereinek konfigurálása és megjelenítése. További információ: <https://manned.org/iwconfig>.

- Az összes interfész paramétereinek és statisztikáinak megjelenítése:

`iwconfig`

- A megadott interfész paramétereinek és statisztikáinak megjelenítése:

`iwconfig {{interface}}`

- A megadott interfész ESSID (hálózati név) beállítása (pl. eth0 vagy wlp2s0):

`iwconfig {{interface}} {{new_network_name}}`

- A megadott interfész működési módjának beállítása:

`iwconfig {{interface}} mode {{ad hoc|Managed|Master|Repeater|Secondary|Monitor|Auto}}`
