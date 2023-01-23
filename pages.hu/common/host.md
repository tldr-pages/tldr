# host

> Domain Name Server keresése. További információ: <https://manned.org/host>.

- Egy domain A, AAAA és MX rekordjainak keresése:

`host {{domain}}`

- Egy domain egy mezőjének (CNAME, TXT,...) keresése:

`host -t {{field}} {{domain}}`

- IP címek fordított keresése:

`host {{ip_address}}`

- Alternatív DNS-kiszolgáló megadása a lekérdezéshez:

`host {{domain}} {{8.8.8.8}}`
