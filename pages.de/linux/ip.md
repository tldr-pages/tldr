# ip

> Zeige und manipuliere routing, Geräte, Policy routing und Tunnel.
> Weitere Informationen: <https://manned.org/ip.8>.

- Zeige Interfaces mit detaillierten Informationen:

`ip {{[a|address]}}`

- Zeige Interfaces mit kurzen Netzwerkinformationen:

`ip {{[-br a|-brief address]}}`

- Zeige Interfaces mit kurzen link layer Informationen:

`ip {{[-br l|-brief link]}}`

- Zeige die Routing Tabelle:

`ip {{[r|route]}}`

- Zeige Nachbarn (ARP Tabelle):

`ip {{[n|neighbour]}}`

- Schalte ein bestimmtes Interface ein oder aus:

`sudo ip {{[l|link]}} {{[s|set]}} {{interface}} {{up|down}}`

- Entferne oder füge eine IP zu einem Interface hinzu:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{interface}}`

- Füge eine Standard Route hinzu:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{interface}}`
