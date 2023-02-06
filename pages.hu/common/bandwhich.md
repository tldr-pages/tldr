# bandwhich

> Az aktuális hálózatkihasználtság megjelenítése folyamat, kapcsolat vagy távoli IP/hostnév szerint. További információ: <https://github.com/imsnif/bandwhich>.

- Csak a távoli címek táblázatának megjelenítése:

`bandwhich --addresses`

- DNS-lekérdezések megjelenítése:

`bandwhich --show-dns`

- Teljes (kumulatív) használat megjelenítése:

`bandwhich --total-utilization`

- Egy adott hálózati interfész hálózati kihasználtságának megjelenítése:

`bandwhich --interface {{eth0}}`

- DNS-lekérdezések megjelenítése egy adott DNS-kiszolgálóval:

`bandwhich --show-dns --dns-server {{dns_server_ip}}`
