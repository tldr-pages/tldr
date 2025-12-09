# traceroute

> Toon het pad dat pakketjes volgen naar een netwerkhost.
> Meer informatie: <https://manned.org/traceroute>.

- Traceroute naar een host:

`traceroute {{example.com}}`

- Schakel IP-adres en hostnaam mapping uit:

`traceroute -n {{example.com}}`

- Specificeer wachttijd in seconden voor antwoord:

`traceroute {{[-w|--wait]}} {{0.5}} {{example.com}}`

- Specificeer het aantal queries per hop:

`traceroute {{[-q|--queries]}} {{5}} {{example.com}}`

- Specificeer de grootte in bytes van het peilpakket:

`traceroute {{example.com}} {{42}}`

- Bepaal de MTU naar de bestemming:

`traceroute --mtu {{example.com}}`

- Gebruik ICMP in plaats van UDP voor tracerouting:

`traceroute {{[-I|--icmp]}} {{example.com}}`
