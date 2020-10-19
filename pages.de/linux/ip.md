# ip

> Zeigt / manipuliert routing, Geräte, Policy routing und Tunnel.

- Zeigt Interfaces mit detailitern Infos:

`ip address`

- Zeigt Interfaces mit kurzer Netzwerk Info:

`ip -brief address`

- Zeigt Interfaces mit kurzer link layer Info:

`ip -brief link`

- Zeigt die Routing Tabelle:

`ip route`

- Zeigt Nachbarn (ARP Tabelle):

`ip neighbour`

- Schaltet Interface ein/aus:

`ip link set {{Interface}} up/down`

- fügt/entfernt eine IP zu einem Interface (hinzu):

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- Fügt eine Standard Route hinzu:

`ip route add default via {{ip}} dev {{interface}}`
