# ip

> Zeige und manipuliere routing, Geräte, Policy routing und Tunnel.
> Weitere Informationen: <https://www.manned.org/ip.8>.

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

`ip {{[l|link]}} set {{interface}} {{up|down}}`

- Entferne oder füge eine IP zu einem Interface hinzu:

`ip {{[a|address]}} add/del {{ip}}/{{mask}} dev {{interface}}`

- Füge eine Standard Route hinzu:

`ip {{[r|route]}} add default via {{ip}} dev {{interface}}`
