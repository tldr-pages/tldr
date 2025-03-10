# ip route show

> Toon subcommando voor IP routeringstabel management.
> Meer informatie: <https://manned.org/ip-route>.

- Toon de routingtabel:

`ip {{[r|route]}} {{[s|show]}}`

- Toon de hoofdrouteringstabel (hetzelfde als eerste voorbeeld):

`ip {{[r|route]}} {{[s|show]}} {{main|254}}`

- Toon de lokale routingtabel:

`ip {{[r|route]}} {{[s|show]}} {{[t|table]}} {{local|255}}`

- Toon Alle routetafels:

`ip {{[r|route]}} {{[s|show]}} {{[t|table]}} {{all|unspec|0}}`

- Toon alleen routes van een bepaald apparaat:

`ip {{[r|route]}} {{[s|show]}} dev {{eth0}}`

- Toon routes binnen een bepaalde scope:

`ip {{[r|route]}} {{[s|show]}} {{[s|scope]}} link`

- Toon de routeringscache:

`ip {{[r|route]}} {{[s|show]}} {{[c|cache]}}`

- Toon alleen IPv6 of IPv4 routes:

`ip {{-6|-4}} {{[r|route]}} {{[s|show]}}`
