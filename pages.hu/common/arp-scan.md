# arp-scan

> ARP-csomagok küldése állomáshelyeknek (IP-címként vagy állomásnévként megadva) a helyi hálózat átvizsgálásához. További információ: <https://github.com/royhills/arp-scan>.

- Az aktuális helyi hálózat letapogatása:

`arp-scan --localnet`

- Egy IP-hálózat átvizsgálása egyéni bitmaszkkal:

`arp-scan {{192.168.1.1}}/{{24}}`

- IP-hálózat átvizsgálása egy egyéni tartományon belül:

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- IP-hálózat átvizsgálása egyéni hálómaszkkal:

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`
