# host

> Zoek de Domain Name Server op.
> Zie ook: `dig`, `resolvectl`, `nslookup`.
> Meer informatie: <https://manned.org/host>.

- Zoek de A-, AAAA- en MX-records van een domein op:

`host {{domein}}`

- Zoek een veld (CNAME, TXT, ...) van een domein op:

`host -t {{veld}} {{domein}}`

- Voer een reverse lookup uit op een IP-adres:

`host {{ip_adres}}`

- Specificeer een alternatieve DNS-server om te bevragen:

`host {{domein}} {{8.8.8.8}}`
