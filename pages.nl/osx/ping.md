# ping

> Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts.
> Meer informatie: <https://keith.github.io/xcode-man-pages/ping.8.html>.

- Ping een specifieke host:

`ping "{{hostnaam}}"`

- Ping een host een specifiek aantal keren:

`ping -c {{aantal}} "{{host}}"`

- Ping een host, met een specifiek interval in seconden tussen de verzoeken (standaard is 1 seconde):

`ping -i {{seconden}} "{{host}}"`

- Ping een host zonder te proberen symbolische namen voor adressen op te zoeken:

`ping -n "{{host}}"`

- Ping een host en laat een bel afgaan wanneer een pakket wordt ontvangen (als je terminal dit ondersteunt):

`ping -a "{{host}}"`

- Ping een host en toon de tijd wanneer een pakket is ontvangen (deze optie is een Apple-toevoeging):

`ping --apple-time "{{host}}"`
