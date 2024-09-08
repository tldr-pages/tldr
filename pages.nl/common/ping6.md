# ping6

> Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts via een IPv6-adres.
> Meer informatie: <https://manned.org/ping6>.

- Ping een host:

`ping6 {{host}}`

- Ping een host een specifiek aantal keren:

`ping6 -c {{aantal}} {{host}}`

- Ping een host met een specifiek interval in seconden tussen verzoeken (standaard is 1 seconde):

`ping6 -i {{seconden}} {{host}}`

- Ping een host zonder te proberen symbolische namen voor adressen op te zoeken:

`ping6 -n {{host}}`

- Ping een host en laat een bel afgaan wanneer een pakket wordt ontvangen (als je terminal dit ondersteunt):

`ping6 -a {{host}}`
