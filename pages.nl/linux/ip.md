# ip

> Toon/manipuleer routing, apparaten, beleidsrouting en tunnels.
> Sommige subcommando's zoals `address` hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://manned.org/ip.8>.

- Toon interfaces met gedetailleerde informatie:

`ip {{[a|address]}}`

- Toon interfaces met beknopte informatie over de netwerklaag:

`ip {{[-br|-brief]}} {{[a|address]}}`

- Toon interfaces met beknopte informatie over de linklaag:

`ip {{[-br|-brief]}} {{[l|link]}}`

- Toon de routingtabel:

`ip {{[r|route]}}`

- Toon buren (ARP-tabel):

`ip {{[n|neighbour]}}`

- Schakel een interface in/uit:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{up|down}}`

- Voeg een IP-adres toe aan een interface of verwijder het ervan:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{ethX}}`

- Voeg een standaardroute toe:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{ethX}}`
