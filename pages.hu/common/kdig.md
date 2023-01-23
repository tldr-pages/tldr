# kdig

> Advanced DNS lookup utility. További információ: <https://www.knot-dns.cz/docs/latest/html/man_kdig.html>.

- A hostnévhez tartozó IP(s) keresése (A rekordok):

`kdig {{example.com}}`

- Adjon meg egy konkrét DNS-kiszolgálót, amelytől lekérdezni kívánja (pl. Google DNS):

`kdig {{example.com}} @{{8.8.8.8}}`

- Egy adott tartománynévhez tartozó konkrét DNS-rekordtípus lekérdezése:

`kdig {{example.com}} {{A|AAAA|NS|SOA|DNSKEY|ANY}}`

- A DNS over TLS (DoT) használatával lekérdezi a hostnévhez (A rekordok) tartozó IP(s) címeket:

`kdig -d @{{8.8.8.8}} +tls-ca +tls-host={{dns.google}} {{example.com}}`

- Egy hostnévhez (A rekordok) tartozó IP(s) keresése DNS over HTTPS (DoH) használatával:

`kdig -d @{{1.1.1.1}} +https +tls-hostname={{1dot1dot1dot1.cloudflare-dns.com}} {{example.com}}`
