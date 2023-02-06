# drill

> Különböző DNS-lekérdezések végrehajtása. További információ: <https://manned.org/drill>.

- A hostnévhez tartozó IP(s) keresése (A rekordok):

`drill {{example.com}}`

- Egy adott tartománynévhez tartozó levelezőszerver(ek) keresése (MX rekord):

`drill mx {{example.com}}`

- Egy adott domain névhez tartozó összes rekordtípus lekérdezése:

`drill any {{example.com}}`

- Alternatív DNS-kiszolgáló megadása a lekérdezéshez:

`drill {{example.com}} @{{8.8.8.8}}`

- Fordított DNS-keresés végrehajtása egy IP-címre (PTR rekord):

`drill -x {{8.8.8.8}}`

- DNSSEC-követés végrehajtása a gyökérkiszolgálóktól a tartománynévig:

`drill -TD {{example.com}}`

- DNSKEY rekord(ok) megjelenítése egy tartománynévhez:

`drill -s dnskey {{example.com}}`
