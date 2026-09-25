# nslookup

> Bevraag naamservers voor verschillende domeinrecords.
> Zie ook: `dig`, `resolvectl`, `host`.
> Meer informatie: <https://manned.org/nslookup>.

- Bevraag de standaard naamserver van je systeem voor een IP-adres (A-record) van het domein:

`nslookup {{example.com}}`

- Bevraag een gegeven naamserver voor een NS-record van het domein:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- Bevraag een reverse lookup (PTR-record) van een IP-adres:

`nslookup -type=PTR {{54.240.162.118}}`

- Bevraag alle beschikbare records (type ANY) met het TCP-protocol:

`nslookup -vc -type=ANY {{example.com}}`

- Bevraag een gegeven naamserver voor het volledige zonebestand (zone transfer) van het domein met het TCP-protocol:

`nslookup -vc -type=AXFR {{example.com}} {{naamserver}}`

- Bevraag een mailserver (MX-record) van het domein, met details van de transactie:

`nslookup -type=MX -debug {{example.com}}`

- Bevraag een gegeven naamserver op een specifiek poortnummer voor een TXT-record van het domein:

`nslookup -port={{poortnummer}} -type=TXT {{example.com}} {{naamserver}}`
