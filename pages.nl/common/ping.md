# ping

> Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts.
> Zie ook: `mtr`.
> Meer informatie: <https://manned.org/ping>.

- Ping een host met IP-adres `10.0.0.1` (Opmerking: `10.0.0.1` kan worden afgekort tot `10.1`):

`ping {{10.0.0.1}}`

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

- Ping een host met een specifiek aantal ([c]) pings, timeout om te [W]achten voor elk antwoord, en totale wachttijd voor de gehele ping-uitvoering:

`ping -c {{aantal}} -W {{seconden}} -w {{seconden}} {{host}}`

- Ping alle IPv6-hosts in het lokale netwerk:

`ping -6 ff02::1%{{eth0}}`
