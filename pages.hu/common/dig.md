# dig

> DNS kereső segédprogram. További információ: <https://manned.org/dig>.

- A hostnévhez tartozó IP(s) keresése (A rekordok):

`dig +short {{example.com}}`

- Részletes válasz egy adott domainhez (A rekordok):

`dig +noall +answer {{example.com}}`

- Egy adott domainnévhez tartozó konkrét DNS-rekordtípus lekérdezése:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Egy adott domain névhez tartozó összes rekordtípus lekérdezése:

`dig {{example.com}} ANY`

- Alternatív DNS-kiszolgáló megadása a lekérdezéshez:

`dig @{{8.8.8.8}} {{example.com}}`

- Fordított DNS-keresés végrehajtása egy IP-címre (PTR rekord):

`dig -x {{8.8.8.8}}`

- A zóna hiteles névkiszolgálóinak keresése és a SOA-rekordok megjelenítése:

`dig +nssearch {{example.com}}`

- Ismétlődő lekérdezések végrehajtása és a teljes nyomkövetési útvonal megjelenítése a tartománynév feloldásához:

`dig +trace {{example.com}}`
