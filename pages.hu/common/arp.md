# arp

> A rendszer ARP-cache-jének megjelenítése és kezelése. További információ: <https://manned.org/arp>.

- Az aktuális ARP-táblázat megjelenítése:

`arp -a`

- A teljes gyorsítótár törlése:

`sudo arp -a -d`

- Egy adott bejegyzés törlése:

`arp -d {{address}}`

- Bejegyzés létrehozása az ARP-táblában:

`arp -s {{address}} {{mac_address}}`
