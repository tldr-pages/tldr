# ip route show

> Toon subcommando voor IP routeringstabel management.
> Meer informatie: <https://manned.org/ip-route>.

- Toon de routingtabel:

`ip route show`

- Toon de hoofdrouteringstabel (hetzelfde als eerste voorbeeld):

`ip route show {{main|254}}`

- Toon de lokale routingtabel:

`ip route show table {{local|255}}`

- Toon Alle routetafels:

`ip route show table {{all|unspec|0}}`

- Toon alleen routes van een bepaald apparaat:

`ip route show dev {{eth0}}`

- Toon routes binnen een bepaalde scope:

`ip route show scope link`

- Toon de routeringscache:

`ip route show cache`

- Toon alleen IPv6 of IPv4 routes:

`ip {{-6|-4}} route show`
