# dog

> Színes kimenettel rendelkezik, támogatja a DNS-over-TLS és DNS-over-HTTPS protokollokat, és képes JSON-t kibocsátani. További információk: <https://dns.lookup.dog>.

- A hostnévhez tartozó IP(s) keresése (A rekordok):

`dog {{example.com}}`

- Egy adott domainnévhez tartozó MX rekordok típusának lekérdezése:

`dog {{example.com}} MX`

- Egy adott DNS-kiszolgáló megadása a lekérdezéshez (pl. Cloudflare):

`dog {{example.com}} MX @{{1.1.1.1}}`

- UDP helyett TCP-n keresztül történő lekérdezés:

`dog {{example.com}} MX @{{1.1.1.1}} --tcp`

- Egy adott tartománynévhez tartozó MX rekordok típusának lekérdezése TCP-n keresztül, explicit argumentumok használatával:

`dog --query {{example.com}} --type MX --nameserver {{1.1.1.1}} --tcp`

- Egy hostnévhez tartozó IP(s) keresése (A rekordok) DNS over HTTPS (DoH) használatával:

`dog {{example.com}} --https @{{https://cloudflare-dns.com/dns-query}}`
