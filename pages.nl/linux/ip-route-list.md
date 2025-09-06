# ip route list

> Toon het subcommando voor het beheer van IP-routetabellen.
> Meer informatie: <https://manned.org/ip-route>.

- Toon de `main` routeringstabel:

`ip {{[r|route]}} {{[l|list]}}`

- Toon de hoofdrouteringstabel (hetzelfde als het eerste voorbeeld):

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{main|254}}`

- Toon de lokale routeringstabel:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{local|255}}`

- Toon alle routeringstabellen:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{all|unspec|0}}`

- Toon alleen routes van een bepaald apparaat:

`ip {{[r|route]}} {{[l|list]}} dev {{eth0}}`

- Toon een lijst van routes binnen een bepaald bereik:

`ip {{[r|route]}} {{[l|list]}} {{[s|scope]}} link`

- Toon de routeringscache:

`ip {{[r|route]}} {{[l|list]}} {{[c|cache]}}`

- Toon alleen IPv6- of IPv4-routes:

`ip {{-6|-4}} {{[r|route]}}`
