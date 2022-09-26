# ip

> Zeige und manipuliere routing, Geräte, Policy routing und Tunnel.
> Weitere Informationen: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Zeige Interfaces mit detaillierten Informationen:

`ip address`

- Zeige Interfaces mit kurzen Netzwerkinformationen:

`ip -brief address`

- Zeige Interfaces mit kurzen link layer Informationen:

`ip -brief link`

- Zeige die Routing Tabelle:

`ip route`

- Zeige Nachbarn (ARP Tabelle):

`ip neighbour`

- Schalte ein bestimmtes Interface ein oder aus:

`ip link set {{interface}} {{up|down}}`

- Entferne oder füge eine IP zu einem Interface hinzu:

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Füge eine Standard Route hinzu:

`ip route add default via {{ip}} dev {{interface}}`
