# dig

> DNS-opzoekhulpprogramma.
> Zie ook: `resolvectl`, `nslookup`, `host`.
> Meer informatie: <https://manned.org/dig>.

- Zoek de IP-adres(sen) op die bij een hostnaam horen (A-records):

`dig +short {{example.com}}`

- Verkrijg een gedetailleerd antwoord voor een gegeven domein (A-records):

`dig +noall +answer {{example.com}}`

- Bevraag een specifiek DNS-recordtype voor een gegeven domeinnaam:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Specificeer een alternatieve DNS-server om te bevragen en gebruik optioneel DNS over TLS (DoT):

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- Voer een reverse DNS-opzoeking uit op een IP-adres (PTR-record):

`dig -x {{8.8.8.8}}`

- Vind autoritatieve naamservers voor de zone en toon SOA-records:

`dig +nssearch {{example.com}}`

- Voer iteratieve queries uit en toon het volledige tracepad om een domeinnaam te herleiden:

`dig +trace {{example.com}}`

- Bevraag een DNS-server via een niet-standaard [p]oort met het TCP-protocol:

`dig +tcp -p {{poort}} @{{dns_server_ip}} {{example.com}}`
