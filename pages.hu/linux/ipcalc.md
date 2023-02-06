# ipcalc

> Egyszerű műveletek és számítások elvégzése IP-címekkel és hálózatokkal. További információ: <https://manned.org/ipcalc>.

- Adott alhálózati maszkkal rendelkező címre vagy hálózatra vonatkozó információk megjelenítése:

`ipcalc {{1.2.3.4}} {{255.255.255.0}}`

- CIDR-jelöléssel megadott cím vagy hálózat információinak megjelenítése:

`ipcalc {{1.2.3.4}}/{{24}}`

- Egy cím vagy hálózat broadcast-címének megjelenítése:

`ipcalc -b {{1.2.3.4}}/{{30}}`

- A megadott IP-cím és hálómaszk hálózati címének megjelenítése:

`ipcalc -n {{1.2.3.4}}/{{24}}`

- Földrajzi információk megjelenítése egy adott IP-címről:

`ipcalc -g {{1.2.3.4}}`
