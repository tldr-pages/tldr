# ping

> Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts.
> Meer informatie: <https://manned.org/ping>.

- Ping host:

`ping {{host}}`

- Ping een host een specifiek aantal keren:

`ping -c {{aantal}} {{host}}`

- Ping host met een specifiek interval in seconden tussen verzoeken (standaard is 1 seconde):

`ping -i {{seconden}} {{host}}`

- Ping host zonder te proberen symbolische namen voor adressen op te zoeken:

`ping -n {{host}}`

- Ping host en laat een bel afgaan wanneer een pakket wordt ontvangen (als je terminal dit ondersteunt):

`ping -a {{host}}`

- Toon ook een bericht als er geen reactie is ontvangen:

`ping -O {{host}}`

- Ping een host met een specifiek aantal pings, timeout (`-W`) voor elk antwoord, en totale tijdslimiet (`-w`) voor de gehele ping-uitvoering:

`ping -c {{aantal}} -W {{seconden}} -w {{seconden}} {{host}}`
