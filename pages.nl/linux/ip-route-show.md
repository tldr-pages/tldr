# ip route show

> Toon subcommando voor IP routeringstabel management.
> Meer informatie: <https://manned.org/ip-route>.

- Toon de routingtabel:

`ip {{[r|route]}} show`

- Toon de hoofdrouteringstabel (hetzelfde als eerste voorbeeld):

`ip {{[r|route]}} show {{main|254}}`

- Toon de lokale routingtabel:

`ip {{[r|route]}} show table {{local|255}}`

- Toon Alle routetafels:

`ip {{[r|route]}} show table {{all|unspec|0}}`

- Toon alleen routes van een bepaald apparaat:

`ip {{[r|route]}} show dev {{eth0}}`

- Toon routes binnen een bepaalde scope:

`ip {{[r|route]}} show scope link`

- Toon de routeringscache:

`ip {{[r|route]}} show cache`

- Toon alleen IPv6 of IPv4 routes:

`ip {{-6|-4}} {{[r|route]}} show`
